# librarys used for full function
from javascript import require, On, Once, AsyncTask, once, off
import time

mineflayer = require('mineflayer')
print("this version of spybot is for cracked servers ")
Address = input("enter server IP: ")


bot = mineflayer.createBot({'host': Address, 'port': 25565, 'username': 'spy', 'hideErrors': False })

@On(bot, 'chat')
def onChat(this, user, message, task, sender, *rest, spammer):
	once(bot, 'login')
	bot.chat('I spawned')
	print(f'{user} said "{message}"')
		
