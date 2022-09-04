from javascript import require, On, Once, AsyncTask, once, off
import time
import os
import random
#information on server and bot
mineflayer = require('mineflayer')
BOT_USERNAME="wullieBot"
bot = mineflayer.createBot({ 'host': '1b1t.me', 'port': 25565, 'username': BOT_USERNAME,  'hideErrors': False })
Login = False

#using other bots for warps and shit
Summon = 'cd bots && python3 niggerBot.py'
Spy = 'cd bots && python3 spy.py '
StashBot = 'cd bots && python3 stashBot.py'


@On(bot, 'chat',)
def onChat(this, user, message, task, *rest):
	#login and chat log, login requied on some server custom password are recomended 

	#	login = True
	#	time.sleep(2)
	#	Login = False
		
	#chat
	print(f'{user} said "{message}"')	
	#commands for wullieBot most only work on 1b1t.me
	if '%help' in message:
        	bot.chat('commands have a "%" prefix, report, penis, hentai, co-ords, imHorny, ip, pt, ping, tps, boobs, nword, noword, yesword, lolliPorn')
			
	if '%report' in message:
		bot.chat('fuck you')
	if '%penis' in message:
		bot.chat('8================D')
	if '%hentai' in message:
		bot.chat('get a life')
	if '%co-ords' in message:
		bot.chat('no im at base')
	if '%imHorny' in message:
		bot.chat('get a life')
	if '%ip' in message:
		bot.chat('127.0.0.1')
	if '%pt' in message:
		bot.chat('!pt wullieBot')
	if '%ping' in message:
		bot.chat('!ping' + {user})
	if '%tps' in message:
		bot.chat('idk press tab, if tps is below 5 blame spyrow')
	if '%niggerBot' in message:
		bot.chat('!nword niggerBot')
	if '%boobs' in message:
		bot.chat('(.) (.)')
	if '%nword' in message:
		bot.chat('nigger')
	if '%noword' in message:
		bot.chat('no')
	if '%yesword' in message:
		bot.chat('yes')
	if '%lolliPorn' in message:
		bot.chat('this interaction has been reported to Scotland yard')
	

			
