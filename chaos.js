const Discord = require('discord.js');
const client = new Discord.Client();

const auth = require('./auth.json');

const serverID = auth.serverID;

client.on('ready', () => {
  console.log('I am ready!');
});

client.on('message', message => {
  if(message.content === '!warframe'){
    addToRole(message,"Warframe");
  }
});

client.login(auth.token);

function addToRole(message, roleName){
  var user = message.member;
  var server = message.guild;
  var roles = server.roles;
  var currRoles = user.roles;
  for(var role in roles){
    if(currRoles.indexOf(role) !== -1){
      message.reply('You are already in the ' + roleName + ' Group');
    }else if(role.name === roleName){
      user.addRole(role);
      message.reply('Added you to the ' + roleName + ' Group');
      console.log('ADDED USER '+ user.name + ' TO ROLE '+ roleName);
      break;
    }
  }
  message.reply('Could not add you to the ' + roleName + ' Group due to an error');
  console.log('[!]ERROR ADDING USER '+ user.name + ' TO ROLE '+ roleName);
}
