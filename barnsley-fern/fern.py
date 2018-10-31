import numpy as np
import matplotlib.pyplot as plt
import random

def f1(x):
    return np.dot(np.array([[0,0],[0,0.16]]),x.T) 

def f2(x):
    return np.dot(np.array([[0.85,0.04],[-0.04,0.85]]),x.T) + np.array([0,1.6])

def f3(x):
    return np.dot(np.array([[0.20,-0.26],[0.23,0.22]]),x.T) + np.array([0,1.6])

def f4(x):
    return np.dot(np.array([[-0.15,0.28],[0.26,0.24]]),x.T) + np.array([0,0.44]) 


def fern(x):
    rnd = random.random()
    if rnd < 0.01:
        return f1(x)
    elif rnd >= 0.01 and rnd < 0.86:
        return f2(x)
    elif rnd >= 0.86 and rnd < 0.93:
        return f3(x)
    elif rnd >= 0.93:
        return f4(x)

n = 1000000
x = np.array([0,0])
y = [[0,0] for i in range(n)]

for i in range(1,n):
    x = fern(x)
    y[i] = x

z = np.array(y)
plt.figure(figsize=(12,12))
plt.axis('off')
plt.plot(z[:,0],z[:,1],'g.', markersize=0.1)
plt.savefig('fern_2.png', dpi=300 , facecolor='black')