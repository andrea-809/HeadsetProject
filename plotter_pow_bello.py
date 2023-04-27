import matplotlib.pyplot as plt
import numpy as np
import json

#------------------------------------------------------------------------
def graph(ax, x, y):
    cont = 0   
    for i in range(2):
        for j in range(3):
            if(i == 1 & j ==2):
               break
            for k in range(5):
                if(cont >= 25): #i dati vanno da 0 a 24 
                    break
                ax[i, j].plot(x, y[cont])
                cont += 1
    """
    l'annidamento di cicli for è necessario per disegnare sulla matrice 2x3 di grafici
    inoltre vogliamo disegnare le curve relative allo stesso sensore sugli stessi assi
    """
#------------------------------------------------------------------------

#------------------------------------------------------------------------
def plot_eeg(nome_file):
  
    #---dichiarazione variabili---
    data = 0
    cont = 0
    y = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    time = []
    #---dichiarazione variabili---

    #---leggo i dati dal file e li converto in  stringhe leggibili---
    result_file = open('met_exp.json')

    data = json.load(result_file)

    result_file.close()
    #---leggo i dati dal file e li converto in  stringhe leggibili---

    for cont in range(len(data)):
        time.append(data[str(cont).zfill(5)]["time"])
        for i in range(25):
            y[i].append(data[str(cont).zfill(5)]["pow"][i])


   
    #---stampo a video---
    x = time

    fig, ax = plt.subplots(2, 3)
    
    #---disegno i grafici sulla matrice di assi---
    graph(ax, x, y)
    ax[0][0].set_title('AF3')
    ax[0][1].set_title('T7')
    ax[0][2].set_title('Pz')
    ax[1][0].set_title('T8')
    ax[1][1].set_title('AF4') 
   #---disegno i grafici sulla matrice di assi---

    plt.show()
    #---stampo a video---

#------------------------------------------------------------------------

plot_eeg('pow_res.json')
