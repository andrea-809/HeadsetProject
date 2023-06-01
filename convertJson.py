## IMPORT LIBRARIES
import matplotlib.pyplot as plt
import numpy as np
import json
from numpy import cov
from scipy.stats import pearsonr
from scipy.stats import spearmanr
import json

### OPENING OF FILES
file = open('/home/sara/SARA/Hand robot - project/Data/EEG/esperimento_1.json')
data = json.load(file)

timeInstants = len(data)

NewData = dict()

for t in data:
    NewData[t] = dict()
    NewData[t]['Theta'] = data[t]['pow'][0:5]
    NewData[t]['Alpha'] = data[t]['pow'][5:10]
    NewData[t]['BetaL'] = data[t]['pow'][10:15]
    NewData[t]['BetaH'] = data[t]['pow'][15:20]
    NewData[t]['Gamma'] = data[t]['pow'][20:25]
    NewData[t]['Time'] = data[t]['time']

nome_file="NewPOW.json"
with open(nome_file, "w") as file_json:
    json.dump(NewData, file_json, indent = 2)

