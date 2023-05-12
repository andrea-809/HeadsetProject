# Apri un file ed inizia a leggerlo:
# formato: 
    # Metrics:.... la prossima linea contiene il titolo
    # reading begins: contiene data in cui è stata effettuata la registrazione
    # data, #,#,#.... metriche.

import re
import json

rwPath = 'C:\\Users\Cerio\OneDrive - Politecnico di Milano\Hackatentativo\BrainData\Esperimento Paper RTSI'
rFileName = 'MetData ' #inizio del nome del file, da completare con ###.txt
expName = "" #nome della fase dell'esperimento
expNr = 0 #numero dell'esperimento, per identificare il file da usare
#ID degli utenti, molto sbatti leggerlo altrimenti
UserIDs = ["M28","F44","F25","M23","F24","F20","F23","M21","M22","M25","M28","F28","M29","M26","M22","F26","M26","M27","F27","F60","M28","M30"]
emotivToJson = {} #inizializzo  libreria

#leggo tutti i file, da 0 a 21
for expNr in range(22):
    file = open(rwPath+'\\'+ rFileName + str(expNr).zfill(3) + ".txt","r") 

    lineNr = 0 #incrementale per le linee di file

    emotivToJson[str(expNr).zfill(3)] ={
                "UserID": UserIDs[expNr],
                "Readings": {}
                }#inserisco dati utente e libreria nestata

    for line in file:
        if re.match("[0-9][0-9]:[0-9][0-9]:[0-9][0-9]+", line):
                splitValues = line.split(',')
                emotivToJson[str(expNr).zfill(3)]["Readings"][str(lineNr).zfill(6)] = {
                        "Phase": expName,
                        "Time": splitValues[0][0:len(splitValues[0])-1],
                        "Engagement": splitValues[1],
                        "Excitement": splitValues[2],
                        "Stress": splitValues[4],
                        "Relaxation": splitValues[5],
                        "Interest": splitValues[6],
                        "Focus": splitValues[7][0:len(splitValues[7])-1]
                    }
                lineNr = lineNr+1
        else:
            if  "begins" not in line and "Metrics:" not in line:
                expName = line[0:len(line)-1]


"""
Recording = {"000":{ 
            "userData": 'M30',
            "readings": {"22.00": {'Phase': 'B', 'Alpha': '1', 'Beta': '2'},
                         "22.01": {'Phase': 'B', 'Alpha': '2', 'Beta': '3'}}
             }}
"""
# Serializing json
json_object = json.dumps(emotivToJson, indent=4)
 
# Writing to sample.json
with open("metData.json", "w") as outfile:
    outfile.write(json_object)

print('finito')






