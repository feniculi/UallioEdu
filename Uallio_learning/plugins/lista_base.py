
#configurazione
id_data="learning_001"

import json
import string
import random
import datetime, json, os, time
from glob    import glob
from os.path import expanduser, join
from os      import getcwd

class plugin_lista(object):
    def __init__(self):
        self.toListen = '/lista'
        print("Comando lista in ascolto")
        pass
            
    def action(self,  param=None, msg=None):
        with open('./data/data_'+str(id_data)+'.json', encoding="utf8") as json_file:
               self.body = json.load(json_file)
        output=''
        if len(param)==1:
            i=0
            for command in self.body["new_action"]:
                i=i+1
                for elem in command["command"]:
                    output= output + str(i) +". "+ str(elem)+"\n"
                    print(output)
        else:
            comando=""
            for i in range(1 , len(param)):
                comando= comando + param[i] + " "
            comando=comando.strip()
            print("Cerco il comando"+str(comando))
            output=''
            i=0
            for command in self.body["new_action"]:
                for elem in command["action"]:
                    if elem==comando:
                        output=output+ "comando: "+str(self.body["new_action"][i]["command"]) + "\nrisposta: "+str(self.body["new_action"][i]["action"])+"\n\n"
                for elem in command["command"]:
                    if elem==comando:
                        output=output+ "comando: "+str(self.body["new_action"][i]["command"]) + "\nrisposta: "+str(self.body["new_action"][i]["action"])+"\n\n"
                i=i+1
            print(output)
        return output
