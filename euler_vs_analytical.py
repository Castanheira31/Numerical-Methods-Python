import matplotlib.pyplot as plt
import numpy as np
import math
#Método de Euler
def h(h): # função  que dita o h
    tempofinal=2
    n=int(tempofinal/h)+1 #Quantidade de "tempos", ou iterações que teremos que fazer menos uma que já vem dentro do "for"
    y0=1 #y(0)
    t0=0 #tempo inicial
    tempo=[] # lista em que estarão todos os tempos adquiridos
    tempo.append(t0)
    y=[] # lista em que estarão todos os "y" adquiridos
    y.append(y0)
    for k in range(1, n):
        t1 = t0 + h
        tempo.append(t1)
        y1 = y0 + h * (-2*y0+t0**2)
        t0 = t1
        y.append(y1)
        y0=y1
    if n<=5:
        plt.plot(tempo,y,color="g",label="Método de Euler (h=0,5)")
    else:
        plt.plot(tempo, y, color="b", label="Método de Euler (h=0,25)")
h(0.25)
#Método analítico
todosost=[] # lista em que estarão todos os tempos adquiridos
todososy=[] # lista em que estarão todos os "y" adquiridos
for tanalitico in np.arange(0,2,0.001): # arange cria um arranjo contendo uma sequência de valores especificados com início (0), fim (2) e passo(0.01) dados
    todosost.append(tanalitico) #adicionará todos os "t" com um passo de 0.001 à lista, esse passo foi escolhido pois se aproxima muito da função real, porém quanto menor for o passo mais preciso será
    yanalitico=1/math.exp(((-tanalitico**4)/4)+1.5*tanalitico) #função encontrada no método analítico
    todososy.append(yanalitico)
print(todosost,todososy)
plt.plot(todosost,todososy,color="r",label="Método analítico")
plt.legend()
plt.show()
