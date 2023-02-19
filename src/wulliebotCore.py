# librarys used for full function
from javascript import require, On, Once, AsyncTask, once, off
import time
import os
import random
import discord
from headerarrays import *

mineflayer = require('mineflayer')
tpsPlugin = require('mineflayer-tps')(mineflayer)


#bot info
print("login is designed for the new microsoft auth system. Do not try loging in whith a older mojang acount")
time.sleep(0.5)
Username = input("enter username: ")
print("this version of wullieBot core is for premuim and cracked servers ")
time.sleep(1)
Address = input("enter server IP: ")

bot = mineflayer.createBot({'auth': 'microsoft', 'host': Address, 'port': 25565, 'username': Username, 'hideErrors': False})
bot.loadPlugin(tpsPlugin) 

#discord intergration begins
TOKEN = ''
intents = discord.Intents().all()
client = discord.Client(intents=intents)
channel = "1015424366332362842" 

@On(bot, 'chat')
def onChat(this, user, message, task, sender, *rest):
   

    # chat commands
    # If you need help understanding what each command does, buy a dictionary.
    # Most commands only work is a version of moo bot is running on the serer.
    # Most of the commands use pattern matching but for commands that require and optinal suffex an `if` ladder is neaded.

    match message:

        #usefull commands
        case '|help':  
            bot.chat(' a list of commands got to https://wullie111.github.io/')

        case '%tps':
            bot.chat(': '+ str(bot.getTps()) )

        case '%ping':
            bot.chat('!ping '+user)

        case '%pt':
            bot.chat('!pt '+user)
            bot.chat(': thats your play time')

        case '%debug': 
            bot.chat(': Health: '+str(bot.health))
            time.sleep(0.5)
            bot.chat(': Hunger: '+str(bot.food))
            time.sleep(0.5)
            bot.chat('!ping')


           
        #joke commands
        case '%gethelp':
            bot.chat(': gonna cry?')

        case '%penis':
            bot.chat(': '+random.choice(Pens))

        case '%ip':
            bot.chat(': server ip is '+Address+' the bot is hosted on 127.0.0.1')

        case '%noword':
            bot.chat(': no')

        case '%yesword':
            bot.chat(': yes')

        case '%co-ords':
            bot.chat(': somewhere between +30m +30m and -30m -30m')
            
        case '%kit':
            bot.chat(user+' has been given '+random.choice(Kit)+' kit')


        # cracked commands
        case '%summonSpy':
            bot.chat('this is designed for cracked servers, if the bot doesnt appere in the next 30 seconds assume the server is not cracked')

        case '%summon':
            bot.chat(': is '+Address+' a premium server? , summon bot only works on cracked servers. This command will not work on premium servers') 


    # start of the if ladder

    #usefull
    if '%git' in message:
         bot.chat(': the projects github https://github.com/wullie111/WullieBotCore')

    if '%report' in message:
        bot.chat(message[8:]+' has been reported, admins will deal with them soon' )

    #joke
    if '%ban' in message:
         bot.chat(': do i look like a fucking admin?')
                
    if '%8ball' in message:
        bot.chat(random.choice(respawnce))

    # user spesific commands
    # Refence to the reserved commands, only these listed in the cases below can use reserved command.
    match user:
        case 'wullie':
            if '%kill' in message:
                bot.chat(': suicide is bad ass')
                bot.chat('/kill')
            if '%stop' in message:
                bot.quit()
            if '%tpa' in message:
                bot.chat(': going to user')
                bot.chat('/tpa wullie')
            if '%home' in message:
                bot.chat(': sent a tp request, you hae 10 seconds to send it')
                time.sleep(10)
                bot.chat('/tpy wullie')



client.run(TOKEN)
                

