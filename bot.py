import discord

client = discord.Client()
#guild = client.get_guild("id")
#notif = guild.get_role("id")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

#@client.event
#async def on_react(reaction, user):
    
    
file = open('../token.tkn', 'r')
for line in file:
    token = line


client.run(token)
