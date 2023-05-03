import matplotlib.pyplot as plt
import numpy as np
import json

#------------------------------------------------------------------------
def graph(ax, x, y):
    #---var declaration---
    cont = 0
    legenda = ["theta", "alpha", "betaL", "betaH", "gamma"]
    #---var declaration---

    for i in range(2):
        for j in range(3):
            #double for used to select the axes to "draw" in
            if(i == 1 & j ==2):
               break
            #y is a matrix: correspondence coloumn <-> sensor/wave related vector of datas (es: y[0] <-> datas from AF3/theta)
            for k in range(5):
                if(cont >= 25): #nunmber of columns is 25 
                    break
                ax[i, j].plot(x, y[cont], label = legenda[k])
                cont += 1
#------------------------------------------------------------------------

#------------------------------------------------------------------------
def plot_eeg(nome_file):
  
    #---var declaration---
    data = 0
    cont = 0
    y = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    time = []
    #---var declaration---
    
    #---reading file---
    result_file = open(nome_file)

    data = json.load(result_file)

    result_file.close()
    #---reading file---
    
    #---isolating time and values to plot---
    for cont in range(len(data)):
        time.append(data[str(cont).zfill(5)]["time"])
        for i in range(25):
            y[i].append(data[str(cont).zfill(5)]["pow"][i])
    #---isolating time and values to plot---
   
    #---print on video output---
    x = time

    #---plotting1---
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    
    colors = ['r', 'g', 'b', 'y', 'c']
    
    
    c =0
    k = 0
    for i in range(25):
    
        ax.bar(x, y[k], zs = k, zdir = 'y', color=colors[i%5], alpha=0.8)
        c +=1
        k+=1
    #---plotting1---



    #---plotting2---
    x = time
    Y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    z = y
    fig2, ax2 = plt.subplots()
    ax2.contourf(x, Y, z)
    #---plotting2---

    #---plotting3---
    plt.style.use('_mpl-gallery-nogrid')
    fig3, ax3 = plt.subplots()

    ax3.imshow(y)
    #---plotting3---
    #graph(ax, x, y)
    """
    ax[0][0].set_title('AF3')
    ax[0][1].set_title('T7')
    ax[0][2].set_title('Pz')
    ax[1][0].set_title('T8')
    ax[1][1].set_title('AF4')
    
    for i in range(2):
        for j in range(3):
            ax[i][j].legend()
    #---plotting---
    """
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()
    #---print on video output---

#------------------------------------------------------------------------

plot_eeg('pow_res.json')
