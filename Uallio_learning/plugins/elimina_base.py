#configurazione
id_data="learning_001"

import json
import string

class plugin_elimina(object):
    def __init__(self):
        self.input = 'text'
        self.toListen = '/elimina'
        print("Il comando /elimina è in ascolto")

    def action(self, param=None, msg=None):
        print (param)
        if len(param)>1:
            com=0
            comando=""
            for i in range(1 , len(param)):
                comando= comando + param[i] + " "
            comando=comando.strip()
            #ricerca doppioni e salvataggio dei dati
            trovato=0
            with open('./data/data_'+str(id_data)+'.json', encoding="utf8") as json_file:
                self.body=json.load(json_file)
                lunghezza=len(self.body['new_action'])
                for i in range(0 , lunghezza):
                    if trovato==1:
                        break
                    for a in self.body['new_action'][i]['command']:
                        #print (str(a) + str(type(a))+ str(comando)+ str(type(comando)))
                        if str(a)==str(comando):
                            trovato=1
                            print ("trovato")
                            self.body["new_action"].pop(i)
                            break
            if trovato==0:
                return("non è presente il comando selezionato")
            with open('./data/data_'+str(id_data)+'.json', mode='w', encoding='utf8') as json_f:
                    json_f.write(json.dumps(self.body, indent=4))
            return("Eliminerò il comando "+ str(comando))
        else:
            return("Per eliminare un comando devi usare questo comando ignorante: elimina [parola di attivazione]")