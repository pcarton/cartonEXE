const Discord = require('discord.js');
const client = new Discord.Client();

const auth = require('./auth.json');

const serverID = auth.serverID;

client.on('error', error => {
  console.log('[Error]');
  console.log(error);
  process.exit(1);
});

client.on('ready', () => {
  console.log('I am ready!');
});

client.on('message', message => {
  if(message.channel.name === "bot"){
    if(message.content === '!warframe'){
      addToRole(message,"Warframe");
    }else if(message.content === '!eso'){
      addToRole(message,"ESO");
    }else if(message.content === '!diablo'){
      addToRole(message,"Diablo");
    }else if(message.content === '!fortnite'){
      addToRole(message,"Fortnite");
    }
  }
});

client.login(auth.token);

function addToRole(message, roleName){
  var user = message.member;
  var server = message.channel.guild;
  var roles = server.roles;
  var currRoles = user.roles;
  console.log("User:"+user+" Server:"+server);
  console.log(roles.size);
  var newRole = roles.find(role => role.name === roleName);
  if(newRole){
    var oldRole = currRoles.find(role => role.name === roleName);
    if(oldRole){
      message.reply('You are already in the '+ roleName + ' group!');
    }else{
      user.addRole(newRole);
      message.reply('Added you to the ' + roleName + ' Group');
      console.log('ADDED USER '+ user.nickname + ' TO ROLE '+ roleName);
    }
  }else{
    message.reply('Could not add you to the ' + roleName + ' Group due to an error');
    console.log('[!]ERROR ADDING USER '+ user.nickname + ' TO ROLE '+ roleName);
  }
}
