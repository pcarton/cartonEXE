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
  var server = message.channel.guild;
  var roles = server.roles;
  var currRoles = user.roles;
  console.log("User:"+user+" Server:"+server);
  console.log(roles.size);
  var newRole = roles.find(role => role.name === roleName);
  if(newRole){
    user.addRole(newRole);
    message.reply('Added you to the ' + roleName + ' Group');
    console.log('ADDED USER '+ user.name + ' TO ROLE '+ roleName);
  }
  message.reply('Could not add you to the ' + roleName + ' Group due to an error');
  console.log('[!]ERROR ADDING USER '+ user.name + ' TO ROLE '+ roleName);
}
