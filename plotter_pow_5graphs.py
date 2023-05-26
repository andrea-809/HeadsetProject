import matplotlib.pyplot as plt
import numpy as np
import json
import datetime
import time

def plot_eeg(nome_file):
  
    #---var declaration---
    data = 0
    cont = 0
    y = [[],[],[],[],[],
         [],[],[],[],[],
         [],[],[],[],[],
         [],[],[],[],[],
         [],[],[],[],[]]
    times = []
    #---var declaration---
    
    #---reading file---
    result_file = open(nome_file)
    data = json.load(result_file)
    result_file.close()
    #---reading file---
    
    #---isolating time and values to plot---
    for count in range(len(data)):
        times.append(data[str(count).zfill(5)]["time"])
        for sensor in range(5):
            for wave in range(5):
                y[sensor*5+wave].append(data[str(count).zfill(5)]["pow"][sensor*5+wave])
    #---isolating time and values to plot---
   
    #---print on video output---
    x = time
    for sensor in range(5):
        plt.figure()
        for wave in range(5):
            plt.plot(x, y[sensor*5+wave])
        print("Figure"+str(sensor))
    plt.show()
    return 0
    #---print on video output---

#------------------------------------------------------------------------

plot_eeg('esperimento_1.json')

#---date to timestamt conversion---
day = "17.05.2023 "
time_human = str(day)+"18:24:57.441270"
date = datetime.datetime.strptime(time_human,"%d.%m.%Y %H:%M:%S.%f")
print(date.timestamp())
#---date to timestamt conversion---