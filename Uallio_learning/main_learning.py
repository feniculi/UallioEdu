#elementi di configurazione
first_name="ilaria"
id_data="learning_001"


import os
import sys
import time
import json
import plugins
import requests
import importlib
from stt_base import vocale_in
from tts_base import sound_out

def on_assistant_message(msg):
	if msg["type"] == 'text':
		command = msg["text"]		
		fn = getattr(pluginCaricati['/rispondi'], 'action')
		ret=fn(command,msg)
		if len(ret)>0:
			riproduci.di(ret)

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
	riproduci=sound_out()
	voce=vocale_in()
	while (1):
		audio_riconosciuto = voce.riconosci(0)
		d=dict()
		f=dict()
		d["text"]=audio_riconosciuto
		d["date"]=time.time()
		d["type"]="text"
		if audio_riconosciuto != "":
			print("\nElaborazione del messaggio in corso")
			on_assistant_message(d)
