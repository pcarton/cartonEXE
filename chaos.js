const Discord = require('discord.js');
const client = new Discord.Client();

const auth = require('./auth.json');

const serverID = auth.serverID;

client.on('ready', () => {
  console.log('I am ready!');
});

client.on('message', message => {
  if (message.content === 'ping') {
    message.reply('pong');
  }
  if(message.content === '!warframe'){
    var user = message.member;
    var server = message.guild;
    var roles = server.roles;
    for(var role in roles){
      if(role.name === "Warframe"){
        user.addRole(role);
        message.reply('Added you to the Warframe Group');
        break;
      }
    }
    message.reply('Could not add you to the Warframe Group due to an error');
  }
});

client.login(auth.token);
