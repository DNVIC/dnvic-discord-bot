import discord
import asyncio


client = discord.Client()
#myguild = await client.fetch_guilds(limit = 150)#270723825417584640
#async for guild in myguild:
#    print(guild.name)
#notif = myguild.get_role(409133998195867650)

guild = 0
notif = 0



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    guild = client.get_guild(270723825417584640)
    notif = guild.get_role(409133998195867650)



#async for guild in client.fetch_guilds(limit=150):
 #   print(guild.name)




@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@client.event
async def on_reaction_add(reaction, user):
    message = reaction.message
    
file = open('../token.tkn', 'r')
for line in file:
    token = line


client.run(token)
