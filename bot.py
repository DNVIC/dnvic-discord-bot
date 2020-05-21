#! /usr/bin/env python3
import discord
import asyncio

#If you're planning on using this, you need to change GUILD-ID and ROLE-ID to the id of your server and the id of the role you want to notify.


client = discord.Client()
#myguild = await client.fetch_guilds(limit = 150)#270723825417584640
#async for guild in myguild:
#    print(guild.name)
#notif = myguild.get_role(409133998195867650)

guild = 0 #guild/server
notif = 0 #role that wants to be notified



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    guild = client.get_guild(GUILD-ID) #guild-id for discord server, get from right clicking server name at top and clicking copy id
    notif = guild.get_role(ROLE-ID) #id of the role you want people to toggle, get from right clicking the role in the roles screen
#async for guild in client.fetch_guilds(limit=150):
 #   print(guild.name)




#@client.event
#async def on_message(message):
#    if message.author == client.user:
#        return

#    if message.content.startswith('$hello'):
#        await message.channel.send('Hello!') 
# test-command

#@client.event
#async def on_reaction_add(reaction, user):
#    message = reaction.message
#    if message.id == 8008531:
#        await user.add_roles(notif, reason="reacted to notif message")
# Attempt at getting it to be a reaction


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    user = message.author
    guild = client.get_guild(GUILD-ID)
    notif = guild.get_role(ROLE-ID)    


    if message.content.startswith('!notifications'):
        notiftrue = True #Boolean to make sure that it toggles on/off and not always on.
        for role in user.roles:
            if role == notif: #Checks if they have the notifications role
                await message.channel.send("Notifications Role Removed")
                await user.remove_roles(notif)
                notiftrue = False  #Sets notiftrue to false so that the role doesnt get added right after
                print("Removed notifications from" + user.name)
        if notiftrue == True: #If they didnt have the role already, this activates
            await message.channel.send("Notifications Role Added")
            print("Added notifications to " + user.name)
            await user.add_roles(notif)

            
    
    


#Takes the token, from a plaintext file in the directory above this one, with the first line just being the token. This is so that the token doesn't accidentally get uploaded to github, which would be bad.
file = open('../token.tkn', 'r')
for line in file:
    token = line


client.run(token)
