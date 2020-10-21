
#configurazione
id_data="learning_001"

import json
import string
import random
import datetime, json, os, time
from glob    import glob
from os.path import expanduser, join
from os      import getcwd

class plugin_list(object):
    def __init__(self):
        self.toListen = '/lista'
        print("Comando lista in ascolto")
        pass
            
    def action(self,  param=None, msg=None):
        with open('./data/data_'+str(id_data)+'.json', encoding="utf8") as json_file:
               self.body = json.load(json_file)
        output=''
        i=0
        for command in self.body["new_action"]:
            i=i+1
            for elem in command["command"]:
                output= output + str(i) +". "+ str(elem)+"\n"
                print(output)
        return output
