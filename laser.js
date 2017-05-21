/*The file to interface with the beam API */

//run 'npm i -S beam-client-node' to get these two things
const BeamClient = require('beam-client-node');
const BeamSocket = require('beam-client-node/lib/ws');
const config = require('./config.json');
const spawn = require('child_process').spawn;

const debug = true;

let userInfo;

const client = new BeamClient();

//OAuth gives permision for all following actions
client.use('oauth',{
  tokens:{
    access: config.OAuth,
    expires: Date.now() + (365 * 24 *60 *60 *1000)
  },
});

//TODO use a GET users/search to get the id of virii, then users/{id} to get his channel

client.request('GET', 'users/current')
.then(response => {
    if(debug) console.log(response.body);
    userInfo = response.body;
    return client.chat.join(response.body.channel.id);
})
.then(response => {
    const body = response.body;
    if(debug) console.log(body);
    return createChatSocket(userInfo.id, userInfo.channel.id, body.endpoints, body.authkey);
})
.catch(error => {
      console.log("Something went wrong:", error);
});

/**
 * Creates a beam chat socket and sets up listeners to various chat events.
 * @param {number} userId The user to authenticate as
 * @param {number} channelId The channel id to join
 * @param {any} endpoints An endpoints array from a beam.chat.join call.
 * @param {any} authkey An authentication key from a beam.chat.join call.
 * @returns {Promise.<>}
 */
function createChatSocket (userId, channelId, endpoints, authkey) {
    const socket = new BeamSocket(endpoints).boot();

    socket.auth(channelId, userId, authkey)
    .then(() => {
        if(debug) console.log('You are now authenticated!');
        // Send a chat message
        return socket.call('msg', ['Hello world!']);
    })
    .catch(error => {
        console.log('Oh no! An error occurred!', error);
    });

    // Listen to chat messages, note that you will also receive your own!
    socket.on('ChatMessage', data => {
        if(debug) console.log('We got a ChatMessage packet!');
        if(debug) console.log(data);
        if(debug) console.log(data.message); // lets take a closer look

        moderate(socket,data);
    });

    // Listen to socket errors, you'll need to handle these!
    socket.on('error', error => {
        console.error('Socket error', error);
    });
}

function moderate(socket,messageData){
  if(debug) console.log("In moderate function");
  //This is how to send the data to be processed by the python
  var moderator = spawn('python', ['hammer.py']);
  moderator.stdin.write(messageToString(messageData.message.message));
  moderator.stdin.end();

  moderator.stdout.on('data', function(data){
    var action = data.toString().split(" ")[0].trim();
    var response = data.toString().split(" ")[1].trim();
    var user = messageData.user_name;
    if(debug){
      console.log("User is:", user);
      console.log("Action to take:",action);
      console.log("Response is: ","@"+user+": "+response);
    }
    if(action === "timeout"){
      if(debug){
        console.log("Need to timeout",user);
      }else{
        socket.timeout(user,config.timeoutDuration);
        socket.msg("@"+user+": "+response);
      }
    }else if(action === "ban"){
      if(debug){
        console.log("Need to ban",user);
      }else{
        socket.timeout(user,config.banDuration);
        socket.msg("@"+user+": "+response);
      }
    }else if(action === "purge"){
      if(debug){
        console.log("Need to purge",user);
      }else{
        socket.purge(user);
        socket.msg("@"+user+": "+response);
      }
    }else if(action === "nothing"){
      if(debug){console.log("No action to take");}
      //THIS SPACE INTENTIONALLY LEFT BLANK
    }
  });

  moderator.stdout.on('end', function(){
    if(debug) console.log("Finished moderate parse");
  });
}

function messageToString(array){
  var result = "";
  for(var index in array){
    var element = array[index];
    result += element.text;
  }
  if(debug) console.log("messageToString is: ", result);
  return result;
}
