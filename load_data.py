import json
from pprint import *
from pathlib import Path

#def read_files(path):
 #   for file in path:
  #      with open('/Users/giuliabartocci/Desktop/CBSD/ARC-master/data/training.json') as f:
  #      d=json.load(f)
#        print(d)

def load_data(data_directories):
    data_directory = Path('/Users/giuliabartocci/Desktop/CBSD/ARC_master/data')
    dict1 = {}
      # Dizionario per memorizzare il contenuto dei file
    dict1['train']=[]
    dict1['test']=[]
    for folder_name in data_directories:
        folder_path = data_directory / folder_name
        if folder_path.is_dir():
            print(f"Scansione della cartella {folder_name}:")
            folder_content = {}  # Dizionario per memorizzare il contenuto dei file nella cartella corrente
            # Itera su tutti i file JSON all'interno della cartella
            for file_path in folder_path.glob('*.json'):
                with open(file_path, 'r') as file:
                    try:
                        # Leggi e analizza il contenuto del file JSON
                        content = json.load(file)
                        
                        # Estrai il nome del file senza estensione
                        # Aggiungi il contenuto al dizionario della cartella
                        for k,val in content.items():
                            if k=='train':
                                dict1['train'].extend(val)
                            if k=='test':
                                dict1['test'].extend(val)

                    except json.JSONDecodeError as e:
                        print(f"Errore durante l'analisi del file {file_path}: {e}")
            # Aggiungi il dizionario della cartella al dizionario generale
        
        else:
            print(f"La cartella {folder_name} non esiste.")
    order_data={}
    for key,values  in dict1.items():
        order_data[key]={'input':[],'output':[]}
        for val in values:
            #print(val)
            for k,v in val.items():
                if k=='input':
                    order_data[key][k].append(v)
                if k=='output':
                    order_data[key][k].append(v)
    return order_data
            
