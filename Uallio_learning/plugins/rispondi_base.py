#configurazione
id_data="learning_001"

import json
import re
import string
import random
import datetime, json, os, time

class plugin_replyrasp(object):
	def __init__(self):
		self.toListen = '/rispondi'
		print("Il riconoscimento dei testi è in ascolto")
		pass
	
	def findWholeWord(self,w):
		return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search
    
	def action(self,  param=None, msg=None):
		with open('./data/data_'+str(id_data)+'.json','r', encoding="utf8") as json_file:
				self.body = json.load(json_file)
				if self.body is not None:
					self.input=param.lower()
					output=''
					for command in self.body["new_action"]:
						for elem in command["command"]:
							if self.findWholeWord(elem.lower())(self.input) is not None:
								output = output + random.choice(command['action'])
					return output
