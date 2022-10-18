# librarys used for full function
from javascript import require, On, Once, AsyncTask, once, off
import time
import os
import random
import discord
from headerarrays import *

# bot info
mineflayer = require('mineflayer')
print("login is designed for the new microsoft auth system. Do not try loging in whith a older mojang acount")
time.sleep(0.5)

Username = input("enter username: ")
Password = input("enter the account password: ")
print("this version of wullieBot core is for premuim and cracked servers ")
time.sleep(1)
Address = input("enter server IP: ")

bot = mineflayer.createBot({'auth': 'microsoft', 'host': Address, 'port': 25565, 'username': Username, 'hideErrors': False})

#arry for random 

@On(bot, 'chat')
def onChat(this, user, message, task, sender, *rest):
    print(f'{user} said "{message}"')

    # chat commands
    # If you need help understanding what each command dose, buy a dictionary.
    # Most commands only work is a version of moo bot is running on the serer.
    # Most of the commands use pattern matching but for commands that require and optinal suffex an if ladder is neaded.

    match message:
        #usefull commands
        case '%help':  
            bot.chat('most command may not work due to moo bot not on said server, commands have a `%` prefix, help, report, gethelp , tps, ping, ip, pt, ban, summon, noword, yesword, co-ords, cancel, debug, github')
            bot.chat(': stop, kill and tpa commands are reserverd')

        case '%tps':
            bot.chat(': idfk press tab')

        case '%ping':
            bot.chat('!ping '+user)

        case '%pt':
            bot.chat('!pt '+user)
            bot.chat(': thats your play time')

        case '%debug':
            bot.chat(': Health: '+str(bot.health))
            time.sleep(0.5)
            bot.chat(': Hunger:'+str(bot.food))
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
            bot.chat(user+' has been given '+random.choice(headerarrays.Kit)+' kit')

        # cracked commands
        case '%summonSpy':
            bot.chat('this is designed for cracked servers, if the bot doesnt appere in the next 30 seconds assume the server is not cracked')

        case '%summon':
            bot.chat(': is '+Address+' a premium server? , summon bot only works on cracked servers. This command will not work on premium servers') 


    # start of the if ladder, could be moved if needed

    #usefull
    if '%git' in message:
         bot.chat(': the projects github https://github.com/wullie111/WullieBotCore')

    if '%report' in message:
        bot.chat(message[:8]+'has been reported, admins will deal with them soon' )

    #joke
    if '%ban' in message:
         bot.chat(': do i look like a fucking admin?')

    if '%8ball' in message:
        bot.chat(random.choice(headerarrys.respawnce))

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
                
        case 'mulfok':
            if '%kill' in message:
                bot.chat('/kill')
            if '%stop' in message:
                bot.quit()
            if '%tpa' in message:
                bot.chat(': going to user')
                bot.chat('/tpa mulfok')
            if '&home' in message:
                bot.chat(': sent a tp request, you have 10 seconds to send it')
                time.sleep(10)
                bot.chat('/tpy mulfok')

    @AsyncTask(start=True)
    def helpme(task):
        while True:
            bot.chat('i have a help command, "%help" for help')
            time.sleep(300)
