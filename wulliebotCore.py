# librarys used for full function
from javascript import require, On, Once, AsyncTask, once, off
import time
import os
import random

# bot info
mineflayer = require('mineflayer')
Username = input("enter username: ")
Password = input("enter the account password: ")
print("this version of wullieBot core is for premuim and cracked servers ")
Address = input("enter server IP: ")

bot = mineflayer.createBot({'auth': 'microsoft', 'host': Address, 'port': 25565, 'username': Username, 'password': Password, 'hideErrors': False })

@On(bot, 'chat')
def onChat(this, user, message, task, sender, *rest):
    print(f'{user} said "{message}"')

    # chat commands.
    # If you need help understanding what each command dose, buy a dictionary.
    # Most commands only work is a version of moo bot is running on the serer.
    match message:
        case '%help':  
            bot.chat('commands have a `%` prefix, help, report, gethelp, penis, tps, nword, ping, ip, pt, ban, summon, noword, yesword, co-ords, cancel, debug, github')
            bot.chat(' stop, kill and tpa commands are reserverd')

        case '%report':
            bot.chat(': fuck you '+user)

        case '%gethelp':
            bot.chat(': gonna cry?')

        case '%penis':
            bot.chat(': 8=====D')

        case '%tps':
            bot.chat(': i have no clue press tab')

        case '%ping':
            bot.chat('!ping '+user)

        case '%ip':
            bot.chat(': server ip is '+Address+' the bot is hosted on 127.0.0.1')

        case '%pt':
            bot.chat('!pt '+user)
            bot.chat(': thats your play time')

        case '%ban':
            bot.chat(': do i look like a fucking admin?')            

        case '%summon':
            bot.chat(': '+Address+' is a premium server, summon bot only works on cracked')

        case '%noword':
            bot.chat(': no')

        case '%yesword':
            bot.chat(': yes')

        case '%co-ords':
            bot.chat(': somewhere between +30m +30m and -30m -30m')

        case '%health':
            bot.chat(': try using %debug')

        case '%cancel':
            bot.chat(':stopping nword spammer')
            spammer = False
            
        case '%debug':
            bot.chat(': Health: '+str(bot.health))
            time.sleep(0.5)
            bot.chat(': Hunger:'+str(bot.food))
            time.sleep(0.5)
            bot.chat('!ping')

        case '%github':
            bot.chat(': the projects github https://github.com/wullie111/WullieBotCore')

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
            if '%home' in message:
                bot.chat(': sent a tp request, you have 10 seconds to send it')
                time.sleep(10)
                bot.chat('/tpy mulfok ')
        
