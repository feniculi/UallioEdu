#configurazione
token='1170852630:AAE1TKr9kS8uNlxPeOkSXRTvTeIObNy85Vw'
id_data="learning_001"

import os
import sys
import json
import time
import plugins
import telepot
import requests
import importlib
from telepot.loop import MessageLoop
from telepot.namedtuple import (InlineKeyboardButton, InlineKeyboardMarkup,
								KeyboardButton, ReplyKeyboardMarkup,
								ReplyKeyboardRemove)
def on_chat_message(msg):
	content_type,chat_type, chat_id = telepot.glance(msg)
	isPhoto=False
	if content_type == 'text':
		command = msg['text']
		print("Ho ricevuto: "+str(command))	
		fn = getattr(pluginCaricati['/rispondi'], 'action')
		ret=fn(command,msg)
		if len(ret)>0:
			bot.sendMessage(chat_id, ret, reply_markup=ReplyKeyboardRemove())
			print("Rispondo: "+str(ret))	

	try:
		toCall = 'action' + ('IsPhoto' if isPhoto else '')
		funz_param=command.split(' ')
		fn = getattr(pluginCaricati[funz_param[0]], toCall)
		ret=fn(funz_param,msg)
		bot.sendMessage(chat_id, ret, reply_markup=ReplyKeyboardRemove())
	except Exception as identifier:
		print("Non esiste nessuna funzione con questo comando:" + str(identifier))
	finally:
		# ignora
		pass

	with open('./data/datastory_'+str(id_data)+'.json', encoding="utf8") as json_file:
		body=json.load(json_file)
	res={"message":msg,"reply":ret}
	body['story'].append(res)
	with open('./data/datastory_'+str(id_data)+'.json', mode='w', encoding='utf8') as json_f:
		json_f.write(json.dumps(body, indent=4))

if __name__ == "__main__":
	pluginCaricati = dict()
	for plugin in dir(plugins):
		if plugin[0:7] == 'plugin_':
			temp = getattr(plugins, plugin)()
			pluginCaricati[temp.toListen] = temp
	bot = telepot.Bot(token)
	answerer = telepot.helper.Answerer(bot)
	MessageLoop(bot, {
		'chat': on_chat_message,
		}).run_as_thread()

	# Enter an infinite loop
	print(' The Telegram Bot is online...')
	while (not time.sleep(10)):
		pass
