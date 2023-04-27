import matplotlib.pyplot as plt
import numpy as np
import json

#------------------------------------------------------------------------
def plot_eeg(nome_file):
  
    #---dichiarazione variabili---
    data = 0
    cont = 0
    y = [[], [], [], [], [], [], []]
    index = [1, 3, 4, 6, 8, 10, 12]
    time = []
    #---dichiarazione variabili---

    #---leggo i dati dal file e li converto in  stringhe leggibili---
    result_file = open('met_exp.json')

    data = json.load(result_file)

    result_file.close()
    #---leggo i dati dal file e li converto in  stringhe leggibili---

    for cont in range(len(data)):
        time.append(data[str(cont).zfill(5)]["time"])
        for i in range(7):
            y[i].append(data[str(cont).zfill(5)]["met"][index[i]])


    #---stampo a video---
    x = time

    fig, ax = plt.subplots()
    for i in range(7):
        ax.plot(x, y[i])
    

    plt.show()
    #---stampo a video---


#------------------------------------------------------------------------

plot_eeg('met_res.json')
