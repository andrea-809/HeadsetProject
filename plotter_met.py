import matplotlib.pyplot as plt
import numpy as np
import json

#------------------------------------------------------------------------
def plot_eeg(nome_file):
  
    #---var declaration---
    data = 0
    cont = 0
    y = [[], [], [], [], [], [], []]
    index = [1, 3, 4, 6, 8, 10, 12]
    time = []
    #---var declaration---

    #---reading file---
    result_file = open(nome_file)

    data = json.load(result_file)

    result_file.close()
    #---reading file---

    for cont in range(len(data)):
        time.append(data[str(cont).zfill(5)]["time"])
        for i in range(7):
            y[i].append(data[str(cont).zfill(5)]["met"][index[i]])


    #---print on video output---
    x = time

    fig, ax = plt.subplots()
    for i in range(7):
        ax.plot(x, y[i])
    

    plt.show()
    #---stampo a video output---
#------------------------------------------------------------------------

plot_eeg('met_res.json')
