# librarys used for full function
from javascript import require, On, Once, AsyncTask, once, off
import time

mineflayer = require('mineflayer')
Username = input("enter username: ")
Password = input("enter the account password: ")
print("this template bot is for cracked servers ")
Address = input("enter server IP: ")


bot = mineflayer.createBot({'auth': 'microsoft', 'host': Address, 'port': 25565, 'username': Username, 'password': Password, 'hideErrors': False })

@On(bot, 'chat')
def onChat(this, user, message, task, sender, *rest, spammer):
	once(bot, 'login')
	bot.chat('I spawned')
	print(f'{user} said "{message}"')
		
