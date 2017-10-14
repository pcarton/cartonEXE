/*The file to interface with the beam API */

//run 'npm i -S beam-client-node' to get these two things
const BeamClient = require('beam-client-node');
const BeamSocket = require('beam-client-node/lib/ws');
const spawn = require('child_process').spawn;

var config;
var configPath;
try{
  config = require('../'+process.argv[2]);
  configPath = process.argv[2];
}catch(e){
  console.log(e);
  config = require('../config.json');
  configPath = "config.json";
}



const debug = config.debug;
var moderationModule = config.moderationOn;
const commandModule = config.commandsOn;

var deathblossomMode = false;

let userInfo;
let channelId = -1;

const client = new BeamClient();

//OAuth gives permision for all following actions
client.use('oauth',{
  tokens:{
    access: config.OAuth,
    expires: Date.now() + (365 * 24 *60 *60 *1000)
  },
});

//get following channel and join its chat
client.request('GET', 'users/current')
.then(response => {
    if(debug) console.log(response.body);
    userInfo = response.body;
    return client.request('GET','channels/'+config.channelUsername);
})
.then(response =>{
  if(debug){
    console.log(response.body);
    return client.chat.join(userInfo.channel.id);
  }else{
    if(response.body){
      channelId = response.body.id;
      console.log("Joining",response.body.name);
      return client.chat.join(channelId);
    }else{
      return client.chat.join(userInfo.channel.id);
    }
  }
})
.then(response => {
    const body = response.body;
    if(debug) console.log(body);
    if(!body.roles.includes('Mod') && !body.roles.includes('Owner')){
      console.log("Cannot moderate this chat");
      moderationModule = false;
    }
    if(!debug && channelId !== -1){
      return createChatSocket(userInfo.id, channelId, body.endpoints, body.authkey);
    }else{
      return createChatSocket(userInfo.id, userInfo.channel.id, body.endpoints, body.authkey);
    }
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
        console.log("Joined chatroom");
        if(config.joinMessage){
          return socket.call('msg', ['BOOTING UP...']);
        }
    })
    .catch(error => {
        console.log('Oh no! An error occurred!', error);
    });

    // Listen to chat messages, note that you will also receive your own!
    socket.on('ChatMessage', data => {
        if(debug) console.log('We got a ChatMessage packet!');
        if(debug) console.log(data);
        if(debug) console.log(data.message); // lets take a closer look
        var roles = data.user_roles;
        log(socket,data,roles);
        if(!roles.includes('Mod') && !roles.includes('Owner')){
          if(!deathblossomMode && moderationModule){
            moderate(socket,data,roles);
          }else if(deathblossomMode){
            deathblossom(socket,data,roles);
          }
        }
        if(commandModule){
          commands(socket,data,roles);
        }
    });

    // Listen to socket errors, you'll need to handle these!
    socket.on('error', error => {
        console.error('Socket error', error);
    });
}

function moderate(socket,messageData,roles){
  //Prepare data before spawning thread
  if(debug) console.log("MODERATE: In moderate function");
  var msgArr = messageToString(messageData.message.message);
  var role = parseRoles(roles);
  var msg = msgArr[0];
  var hasLink = msgArr[1]; //TODO make link handler
  var toPython = messageData.user_name + " " + role + " " + msg;
  if(debug) console.log("\tMODERATE: Input to python:", toPython);

  if(hasLink){
    //This is how to send the data to be processed by the python
    var linkHandler = spawn('python3', ['modules/ganon.py', configPath]);

    linkHandler.stdin.write(messageData.user_name + " " + role);
    linkHandler.stdin.end();

    linkHandler.stdout.on('data', function(data){
      var pythonOut = data.toString().trim();
      if(debug) console.log("\tLINKHANDLER: From python:",pythonOut);
      var action = pythonOut.split(" ")[0];
      var user = pythonOut.split(" ")[1];
      var indexOfSpace1 = pythonOut.indexOf(" ");
      var indexOfSpace2 = pythonOut.indexOf(" ",indexOfSpace1+1);
      var response = pythonOut.substr(indexOfSpace2);
      if(indexOfSpace2 === -1){
        response = "";
      }
      if(debug){
        console.log("\tLINKHANDLER: User is:", user);
        console.log("\tLINKHANDLER: Action to take:",action);
        console.log("\tLINKHANDLER: Response is: ","@"+user+": "+response);
      }
      //Parse the actions and take action if needed
      if(action === "timeout"){
        timeout(socket,user,response,msg);
      }else if(action === "ban"){
        ban(socket,user,response,msg);
      }else if(action === "purge"){
        purge(socket,user,response,msg);
      }else if(action === "nothing"){
        if(debug){console.log("\tLINKHANDLER:No action to take");}
        //THIS SPACE INTENTIONALLY LEFT BLANK
      }
    });

    linkHandler.stdout.on('end', function(){
      if(debug) console.log("MODERATE: Finished moderate parse");
    });

  }else{
    //This is how to send the data to be processed by the python
    var moderator = spawn('python3', ['modules/hammer.py', configPath]);

    moderator.stdin.write(toPython);
    moderator.stdin.end();

    moderator.stdout.on('data', function(data){
      var pythonOut = data.toString().trim();
      if(debug) console.log("\tMODERATE: From python:",pythonOut);
      var action = pythonOut.split(" ")[0];
      var user = pythonOut.split(" ")[1];
      var indexOfSpace1 = pythonOut.indexOf(" ");
      var indexOfSpace2 = pythonOut.indexOf(" ",indexOfSpace1+1);
      var response = pythonOut.substr(indexOfSpace2);
      if(indexOfSpace2 === -1){
        response = "";
      }
      if(debug){
        console.log("\tMODERATE: User is:", user);
        console.log("\tMODERATE: Action to take:",action);
        console.log("\tMODERATE: Response is: ","@"+user+": "+response);
      }
      //Parse the actions and take action if needed
      if(action === "timeout"){
        timeout(socket,user,response,msg);
      }else if(action === "ban"){
        ban(socket,user,response,msg);
      }else if(action === "purge"){
        purge(socket,user,response,msg);
      }else if(action === "nothing"){
        if(debug){console.log("\tMODERATE:No action to take");}
        //THIS SPACE INTENTIONALLY LEFT BLANK
      }
    });

    moderator.stdout.on('end', function(){
      if(debug) console.log("MODERATE: Finished moderate parse");
    });
  }
}

function ban(socket,user,response,msg){ //TODO check that the call completed successfully
  if(debug){
    console.log("Need to ban",user);
  }else{
    socket.call('timeout',[user,config.banDuration]); //need to timeout for 1 to unban
    if(!config.silentBans && response !== null) socket.call('msg',["@"+user+": "+response]);
    console.log("[BAN]",user,"Message:",msg);
  }
}

function purge(socket,user,response,msg){ //TODO check that the call completed successfully
  if(debug){
    console.log("Need to purge",user);
  }else{
    socket.call('purge',[user]);
    if(!config.silentBans && response !== null) socket.call('msg',["@"+user+": "+response]);
    console.log("[PURGE]",user,"Message:",msg);
  }
}

//To unban, use a duration of 1 with this function
function timeout(socket,user,response,msg,duration){
  //TODO check that the call completed successfully
  if(debug){
    console.log("Need to timeout",user);
  }else{
    if(duration){
      socket.call('timeout',[user,duration]);
    }else{
      socket.call('timeout',[user,config.timeoutDuration]);
    }
    if(!config.silentBans && response !== null) socket.call('msg',["@"+user+": "+response]);
    console.log("[TIMEOUT]",user,"Message:",msg);
  }
}

function unban(socket,user){
  console.log("[UNBANNED]",user);
  timeout(socket,user,"You have been unbanned", "<TO UNBAN>",1);
}

function messageToString(array){
  var result = "";
  var hasLink = false;
  for(var index in array){
    var element = array[index];
    result += element.text;
    if(element.type === "link"){
      hasLink = true;
    }
  }
  if(debug) console.log("\tMESSAGE2STRING: messageToString is:", result);
  return [result, hasLink];
}


function commands(socket,messageData,roles){
  if(debug) console.log("COMMANDS: In commands function");
  var msg = messageToString(messageData.message.message)[0];
  var role = "Normal";
  var username = messageData.user_name;

  //Send command to python script
  if(msg.charAt(0) != '!'){
    return;
  }else{
    role = parseRoles(roles);
    var handleCmds = spawn('python3', ['modules/centurion.py', configPath]);
    var toPython = username + " " + role + " " + msg;
    if(debug) console.log("\tCOMMANDS: Input to python:", toPython);
    handleCmds.stdin.write(toPython);
    handleCmds.stdin.end();

    handleCmds.stdout.on('data', function(data){
      var pythonOut = data.toString().trim();
      if(debug) console.log("\tCOMMANDS: From python:",pythonOut);
      var action = pythonOut.split(" ")[0];
      var user = pythonOut.split(" ")[1];
      var indexOfSpace1 = pythonOut.indexOf(" ");
      var indexOfSpace2 = pythonOut.indexOf(" ",indexOfSpace1+1);
      var response = pythonOut.substr(indexOfSpace2);
      if(indexOfSpace2 === -1){
        response = "";
      }
      if(debug){
        console.log("\tCOMMANDS: User is:", user);
        console.log("\tCOMMANDS: Action to take:",action);
        console.log("\tCOMMANDS: Response is: ","@"+user+": "+response);
      }
      //Parse the actions and take action if needed
      if(action === "timeout"){
        timeout(socket,user,response,msg);
      }else if(action === "ban"){
        ban(socket,user,response,msg);
      }else if(action === "purge"){
        purge(socket,user,response,msg);
      }else if(action === "respond"){
        socket.call('msg', [response]);
      }else if(action === "unban"){
        unban(socket,user);
      }else if(action === "deathblossom"){
        if(!deathblossomMode){
          console.log("[DEATHBLOSSOM ON]");
          socket.call('msg', ["Initializing the DeathBlossom..."]);
          socket.call('msg', ["Now Banning on sight. Lurking in the shadows is recommended"]);
          deathblossomMode = true;
        }else{
          console.log("[DEATHBLOSSOM OFF]");
          socket.call('msg', ["DeathBlossom Deactivated."]);
          deathblossomMode = false;
        }
      }else if(action === "nothing"){
        if(debug){console.log("\tCOMMANDS: No action to take");}
        //THIS SPACE INTENTIONALLY LEFT BLANK
      }
    });

    handleCmds.stdout.on('end', function(){
      if(debug) console.log("COMMANDS: Finished command parse");
    });
  }

}

function parseRoles(roleArr){
  var result = "Normal";
  for(var index in roleArr){
    var role = roleArr[index];
    //TODO parse the remaining Mixer roles'
    if(role === "Owner"){
      result = "Caster";
    }else if(role === "Mod" && result !== "Caster"){
      result = "Mod";
    }else if(role == "User" && result !== "Caster" && result !== "Mod"){
      result = "Normal";
    }
  }
  return result;
}

function log(socket,messageData,roles,action){
  if(debug) console.log("LOG: In logs function");
  var msg = messageToString(messageData.message.message)[0];
  var role = parseRoles(roles);
  var username = messageData.user_name;
  if(action){
    //TODO for the moderation/other actions
  }else{
    console.log("[CHAT] "+username + ": "+msg); //TODO add timestamp? or only in log?
  }
  //TODO connect with python module
}

function deathblossom(socket, messageData, roles){
  var role = parseRoles(roles);
  var username = messageData.user_name;
  timeout(socket, username, null, null, 86400); //Time out for one day

}
