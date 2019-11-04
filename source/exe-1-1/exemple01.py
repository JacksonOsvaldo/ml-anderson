#!/usr/bin/env python3
#-*- ecoding: utf-8 -*-

import pandas as pd
import numpy as np
import math as mt
import matplotlib.pyplot as plt
from pandas import *
from numpy import *



#Exemple and resolution question of number 01

"""
Gerando o Gráfico dos vetores de teste

t = np.sin(2*np.pi*x) + ruido
ruido = t - np.sin(2*np.pi*x)

"""

x = [0.1387, 0.2691, 0.3077, 0.3625, 0.4756, 0.5039, 0.5607, 0.6468, 0.7490, 0.7881]
t = [0.8260, 1.0469, 0.7904, 0.6638, 0.1731, -0.0592, -0.2433, -0.6630, -1.0581, -0.8839]
ruido = []
curva=[]



for i in range(10):
    
    # ruido.append(t[int(i)]-np.sin(2*np.pi*x[int(i)])) # Cálculo do ruido

    curva.append(np.sin(2*np.pi*x[int(i)])) #Cáuculo para curva


plt.scatter(x,t)
plt.plot(x,curva,color='#17a589')

# plt.axis([0, 1, -1, 1]) #Caso queira mudar o intervalo do gráfico, nos eixos X e Y, basta tirar o comentário dessa parte do código.

plt.xlabel('x')
plt.ylabel('t')
plt.title('Figure 1.2')
plt.show()