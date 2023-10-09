const fs = require('fs');
const { Client } = require('discord.js-selfbot-v13');
const client = new Client({
    checkUpdate: false,
});

client.on('ready', async () => {
  console.log(`${client.user.username} is ready!`);
})

client.on('messageCreate', async (message) => {
    if (message.content === '!top') { // COMMAND 
      try {
        await message.guild.members.fetch(); // Fetch all members in the server
        const members = message.guild.members.cache;
        const userArray = members.map((member) => `${member.user.id} | ${member.user.username}`);
        const userString = userArray.join('\n');
        fs.writeFile('userids.txt', userString, (err) => {
          if (err) throw err;
          console.log('User IDs and usernames saved to file!');
        });
      } catch (err) {
        console.error('Error fetching members:', err);
      }
    }
  });


client.login('ENTER YOUR ACCOUNT TOKEN HERE');