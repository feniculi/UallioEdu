#configurazione
id_data="learning_001"

import json
import string

class plugin_impara(object):
    def __init__(self):
        self.input = 'text'
        self.toListen = '/impara'
        print("Il comando /impara è in ascolto")

    def action(self, param=None, msg=None):
        print (param)
        domanda_s=''
        risposta_s=''
        domanda=0
        if len(param)>1:
   
            for i in range(1 , len(param)):
                print(i)
                if param[i]!="-" and domanda==0:
                    domanda_s= domanda_s + param[i]
                    if param[i+1]!="-":
                        domanda_s= domanda_s + " "
                    print (domanda_s)
                else:
                    if param[i]=="-":
                        domanda=1
                    else:
                        risposta_s= risposta_s + param[i] + ' '
            risposta_s=risposta_s.strip()
            domanda_s= domanda_s.strip()

            #ricerca doppioni e salvataggio dei dati
            trovato=0
            with open('./data/data_'+str(id_data)+'.json', encoding="utf8") as json_file:
                self.body=json.load(json_file)
                for i in range(0 , len(self.body['new_action'])):
                    for a in self.body['new_action'][i]['command']:
                        if a==domanda_s:
                            trovato=1
                            self.body['new_action'][i]['action'].append(risposta_s.lower())
                            self.body['new_action'][i]['taught_by'].append(msg["from"]["first_name"])
                if trovato==0:
                    res={'command': [domanda_s.lower()], 'action':[risposta_s],'taught_by':[msg["from"]["first_name"]]}
                    self.body['new_action'].append(res)    
            with open('./data/data_'+str(id_data)+'.json', mode='w', encoding='utf8') as json_f:
                    json_f.write(json.dumps(self.body, indent=4))
            return("Bella lo terrò in mente e quando dirai "+ domanda_s + ", dirò " + risposta_s)
        else:
            return("Per impararmi le cose devi usare questo comando ignorante: impara [parola di attivazione] [risposta]")