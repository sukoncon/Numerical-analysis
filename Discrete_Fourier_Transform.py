# -*- coding: utf-8 -*-
"""
SuChouer 
Discrete Fourier Transform
"""
# Discrete Fourier Transform (DFT)
# FB - 20141227

import math
import cmath
import numpy as np
import matplotlib.pyplot as plt

pi = cmath.pi


        



# Initialise a sin signal x = 2*pi*f*t
f = 1
t = np.linspace(0,1,6)
t = t[:-1]
X = []
for time in t:
    #X.append(math.sin(2*pi*f*time))
    X.append(np.exp(2*pi*f*time))
    
    
   
    
def DFT(X):
    Y = []
    N = len(X)
    for k in range(N):
        # compute y_k
        y_k = 0
        for j in range(N):
            y_k += X[j]*cmath.exp(- 1j*2*cmath.pi/N*j*k)
        y_k = y_k/cmath.sqrt(N)
        Y.append(y_k)
    return Y



def DFT_Function(t,X,Y):
    N = len(X)
    c = t[0]
    d = math.ceil(t[N-1])
    x = np.linspace(c,d,100)
    # Initialise the interpolating function 
    P = 0
    plt.figure(1) 
    for k in range(N):
        a = Y[k].real
        b = Y[k].imag
        # The interpolation function is
        #P += (a + b*1j) * np.exp(1j*2*cmath.pi*k*(x-c)/(d-c))
        # Visualise evrey component of DFT
        #p = (a + b*1j)*np.exp(1j*2*pi*k*x)
        p = (a + b*1j) * np.exp(1j*2*cmath.pi*k*(x-c)/(d-c))
        plt.figure(1)

        #plt.scatter(t,X,color='red')  
        #plt.plot(x,P)
        plt.scatter(t,X)
        plt.plot(x,p,linestyle=':')
        P += p
    
    P = P/cmath.sqrt(N)
    plt.plot(x,P)
    return(x,P)
    
    
    
  

Y = DFT(X)

x,P = DFT_Function(t,X,Y)
plt.figure(2)
plt.scatter(t,X)
plt.plot(x,P)
plt.xlabel('Time')
plt.ylabel('Signal')
plt.show()



