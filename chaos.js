var Discord = require('discord.io');
var logger = require('winston');
var auth = require('./auth.json');
const serverID = auth.serverID;

// Configure logger settings
logger.remove(logger.transports.Console);
logger.add(logger.transports.Console, {
    colorize: true
});
logger.level = 'debug';
// Initialize Discord Bot
var bot = new Discord.Client({
   token: auth.token,
   autorun: true
});
bot.on('ready', function (evt) {
    logger.info('Connected');
    logger.info('Logged in as: ');
    logger.info(bot.username + ' - (' + bot.id + ')');
});

bot.on('message', function (user, userID, channelID, message, evt) {
    // Our bot needs to know if it will execute a command
    // It will listen for messages that will start with `!`
    if (message.substring(0, 1) == '!') {
      parseCommand(user, userID, channelID, message, evt);
    }
});

function parseCommand(user, userID, channelID, message, evt){
  var args = message.substring(1).split(' ');
  var cmd = args[0];
  args = args.splice(1);
  switch(cmd) {
      // !ping
      case 'ping':
          bot.sendMessage({
              to: channelID,
              message: 'Pong!'
          });
      break;
      case 'getServerID':
          var channelObj = Discord.Endpoints.CHANNEL(channelID);
          var serverObj = Discord.Endpoints.SERVERS(channelObj.guild_id);
          bot.sendMessage({
              to: channelID,
              message: "SERVERID:" + serverObj.id
          });
      break;
      case 'warframe':

        bot.addToRole({
          "serverID": serverID,
          "userID": userID,
          "roleID": "Warframe"
        });
      break;
   }
}
