meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD": "Reaccion a algo gracioso",
            "ROFL":  "una respuesta a una broma",
            "SHEESH":  "ligera desaprobación",
            "CREEPY": "aterrador, siniestro",
            "AGGRO":  "ponerse agresivo/enojado"
            }
word = input("Escribe una palabra que no entiendas (mayusculas):").upper()
             
if word in meme_dict.keys():
     print(word,meme_dict[word])
else:
     print("Esa palabra no existe en el diccionario")
