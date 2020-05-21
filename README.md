# dnvic-discord-bot
Discord bot for my discord server

If you want to use this, you need a server (you can use a computer but most computers aren't on 24/7), a server with a notifications role, and a discord bot.

# Instructions

Step 1 Making the bot:

go here: https://discord.com/developers/applications \n
make an application (name and picture don't matter at all so dont make a picture for this one) \n
click on bot on the left side \n
click add a bot \n
click yes do it \n
change the username and picture to what you want your bots usernames/pictures to be \n
click on oauth2 on the side \n
under scopes click on bot \n 
under bot click on administrator (you can view the source code so its not going to destroy the server. If you want, it probably will work with send messages, read message history, and manage roles) \n
click on the url under scopes and invite it to your server \n

Step 2 Installing python and the bot:

Install python 3 (3.5.3 and up should work)
If you don't know how to install it, go here (https://wiki.python.org/moin/BeginnersGuide/Download)


Once python is installed, go into command line/terminal and type one of these two things
```
    # Linux/macOS
    python3 -m pip install -U discord.py

    # Windows
    py -3 -m pip install -U discord.py
```
Create a folder named discord-bot (or something else), and in that folder create another folder named src (or something else again)

Linux:
In the terminal in the discord-bot folder (if you dont have git installed, install it), type 
```
git clone https://github.com/DNVIC/dnvic-discord-bot.git src
```
In the above command rename src to whatever you named your folder

Other:
Download this repository and copy it over to the src (or whatever else folder)

Step 3 Setting up the bot:

Go back to the discord link, and go back into the bot page. Once you're there, click copy under the token section, and put that token in the first line of a plaintext file called token.tkn in the discord-bot folder.

Edit the bot.py file and replace GUILD-ID and ROLE-ID with their respective ids (instructions in the file)

Run the python file
