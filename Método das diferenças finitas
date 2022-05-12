import numpy as np
import matplotlib.pyplot as plt
#Solução Numérica
def n(n): #função que dita o n
    a=0
    b=2
    matrizB=np.zeros(n)
    matrizB[0]=1
    matrizB[-1]=2.72
    y=matrizB
    h=(b-a)/(n)
    x=np.linspace(a,b,num=n)
    matrizA=np.zeros((n,n))
    matrizA[0,0]=1
    matrizA[-1,-1]=1
    for i in range(1, n-1):
        matrizA[i, i + 1] = 1
        matrizA[i, i - 1] = -1
    for j in range(0,15):
        for k in range(1, n-1):
            matrizB[k]=2*h*y[k]*(x[k]**3-1.5)
        y = np.linalg.solve(matrizA, matrizB) #Multiplica a matriz B pela inversa da matriz A
    # Solução analítica
    xsoluçãoanalitica = np.linspace(0, 2, 1000)
    ysoluçãoanalitica = np.exp(xsoluçãoanalitica ** 4 / 4 - 1.5 * xsoluçãoanalitica)
    # Plotagem do gráfico
    if n==10:
        plt.plot(x, y, "r", label="Método das diferenças finitas com 10 pontos")
        plt.plot(xsoluçãoanalitica,ysoluçãoanalitica,"b",label="Solução analítica")
    elif n==100:
        plt.plot(x, y, "r", label="Método das diferenças finitas com 100 pontos")
        plt.plot(xsoluçãoanalitica, ysoluçãoanalitica, "b", label="Solução analítica")
    else:
        plt.plot(x, y, "r", label="Método das diferenças finitas com 1000 pontos")
        plt.plot(xsoluçãoanalitica, ysoluçãoanalitica, "b", label="Solução analítica")
    plt.grid()
    plt.xlabel("Eixo x")
    plt.ylabel("Eixo y")
    plt.legend(loc="upper center")
    plt.show()
n(10)
n(100)
n(1000)
