import matplotlib.pyplot as plt
import numpy as np

#------------------------------------------------------------------------
def string_to_list(str, list, x):
    temp = str.split(', ')

    #modifichiamo il primo valore  {'pow': [num --> num
    cambio = temp[0]
    cambio = cambio.split('[')[1]
    temp[0] = cambio
    #fine modifica -----------------------------------

    #modifichiamo il 25esimo valore num] --> num
    cambio = temp[24]
    cambio = cambio.replace(']', '')
    temp[24] = cambio
    #fine modifica ---------------------------- 

    #modifichiamo il valore del tempo 'time': 1679664721.3175} 
    time = temp.pop()
    time = time.replace("'time': ", '')
    time = time.replace('}\n', '')
    time = float(time)
    x.append(time)
    #fine modifica ------------------------------------------

    for i in range(len(temp)):
        temp[i] = float(temp[i])

    list = list + temp
    return list
#------------------------------------------------------------------------

#------------------------------------------------------------------------
def select_data(list, dest, type):
    
    #"AF3/theta"
    if(type == 0):
        i = 0
        while(i < len(list)):
            dest.append(list[i])
            i += 25
        return dest
    
    #"AF3/alpha"
    if(type == 1):
        i = 1
        while(i < len(list)):
            dest.append(list[i])
            i += 25
        return dest
    
    #"AF3/betaL"
    if(type == 2):
        i = 2
        while(i < len(list)):
            dest.append(list[i])
            i += 25
        return dest
    
    #"AF3/betaH"
    if(type == 3):
        i = 3
        while(i < len(list)):
            dest.append(list[i])
            i += 25
        return dest
    
    #"AF3/gamma"
    if(type == 4):
        i = 4
        while(i < len(list)):
            dest.append(list[i])
            i += 25
        return dest
    
    #"T7/theta"
    if(type == 5):
        i = 5
        while(i < len(list)):
            dest.append(list[i])
            i += 25
        return dest
    
    #"T7/alpha"
    if(type == 6):
        i = 6
        while(i < len(list)):
            dest.append(list[i])
            i += 25
        return dest
    
    #"T7/betaL"
    if(type == 7):
        i = 7
        while(i < len(list)):
            dest.append(list[i])
            i += 25
        return dest
    
    #"T7/betaH"
    if(type == 8):
        i = 8
        while(i < len(list)):
            dest.append(list[i])
            i += 25
        return dest
    
    #"T7/gamma"
    if(type == 9):
        i = 9
        while(i < len(list)):
            dest.append(list[i])
            i += 25
        return dest
    
    #"Pz/theta"
    if(type == 10):
        i = 10
        while(i < len(list)):
            dest.append(list[i])
            i += 25
        return dest
    
    #"Pz/alpha"
    if(type == 11):
        i = 11
        while(i < len(list)):
            dest.append(list[i])
            i += 25
        return dest
   
    #"Pz/betaL"
    if(type == 12):
        i = 12
        while(i < len(list)):
            dest.append(list[i])
            i += 25
        return dest
    
    #"Pz/betaH"
    if(type == 13):
        i = 13
        while(i < len(list)):
            dest.append(list[i])
            i += 25
        return dest
    
    #"Pz/gamma"
    if(type == 14):
        i = 14
        while(i < len(list)):
            dest.append(list[i])
            i += 25
        return dest
    
    #"T8/theta"
    if(type == 15):
        i = 15
        while(i < len(list)):
            dest.append(list[i])
            i += 25
        return dest
    
    #"T8/alpha"
    if(type == 16):
        i = 16
        while(i < len(list)):
            dest.append(list[i])
            i += 25
        return dest
    
    #"T8/betaL"
    if(type == 17):
        i = 17
        while(i < len(list)):
            dest.append(list[i])
            i += 25
        return dest
    
    #"T8/betaH"
    if(type == 18):
        i = 18
        while(i < len(list)):
            dest.append(list[i])
            i += 25
        return dest
    
    #"T8/gamma"
    if(type == 19):
        i = 19
        while(i < len(list)):
            dest.append(list[i])
            i += 25
        return dest

    #"AF4/theta"
    if(type == 20):
        i = 20
        while(i < len(list)):
            dest.append(list[i])
            i += 25
        return dest
    
    #"AF4/alpha"
    if(type == 21):
        i = 21
        while(i < len(list)):
            dest.append(list[i])
            i += 25
        return dest
    
    #"AF4/betaL"
    if(type == 22):
        i = 22
        while(i < len(list)):
            dest.append(list[i])
            i += 25
        return dest
    
    #"AF4/betaH"
    if(type == 23):
        i = 23
        while(i < len(list)):
            dest.append(list[i])
            i += 25
        return dest
    
    #"AF4/gamma"
    if(type == 24):
        i = 24
        while(i < len(list)):
            dest.append(list[i])
            i += 25
        return dest

    #gestione dell'errore 
    else:
        print('ERRORE: assegnare correttamente indice')
        return None
#------------------------------------------------------------------------

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
    y = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    time = []
    list = []
    #---dichiarazione variabili---

    #---leggo i dati dal file e li converto in  stringhe leggibili---
    result_file = open(nome_file)

    while(True):
        data = result_file.readline()
        if(data == ''):
            break
        list = string_to_list(data, list, time)
        """
        string_to_list prende in ingresso il valore appena letto "data" e scrive (ripulendo)
        i valori della frequenza in list (array di molti elementi), scrive in time i valori di tempo
        """
   
    result_file.close()
    #---leggo i dati dal file e li converto in  stringhe leggibili---


    #---preparo_i_dati---
    for i in range(25):
        select_data(list, y[i], i)
        """
        i valori in list sono confusi: essendo concatenati, vogliamo isolare solo quelli relativi ad uno specifico sensore
        e ad una specifica frequenza. Ad ogni indice [0, 24] è associato un tipo di valore che viene salvato nella riga
        corrispondente della matrice y (le colonne corrispondono invece ad istanti di tempo uguali)
        """
    #---preparo_i_dati---

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

plot_eeg('risultati.txt')
