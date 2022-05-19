import matplotlib
import numpy as np
import matplotlib.pyplot as plt
Tb=20
Tt=100
Td=30
Ti=25
Te=30
Td=30
L=1
alfa=0.0155
n=5
dx=L/(n)
dy= L/(n)
s=1/20
dt=s/(alfa*1/dx**2+1/dy**2)
tTotal=20
x=np.linspace(0,1,n)
y=x
T=np.ones(n+1,n+1)*Ti
T[2:n,1]=Te
T[2:n,n+1]=Td
T[1,2:n]=Tb
T[n+1,2:n]=Tt
t=0
k=0
while t<tTotal:
    T0=T
    for i in range(2,n):
        for j in range(2,n):
            T[i,j]=T0[i,j]+dt*alfa*((T0[i-1,j]-2*T0[i,j]+T0[i+1,j]))/dx**2+(T0[i,j-1]-2*T0[i,j]+T0[i,j+1]/dy**2)
    t=t+dt
matplotlib.pyplot.contour(x,y,T,20)
