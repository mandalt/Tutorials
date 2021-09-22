#kinesin walking on microtubule

import numpy as np
import matplotlib.pyplot as plt
from random import random
from math import log

kfor=1.0      #rate of taking a step forward
kback=.6      #rate of taking a step backward
kdetach=0.08  #rate of getting detached
iter_t=100
trials=10000
D=[]
dis=np.zeros((iter_t,trials))
time=np.zeros((iter_t,trials))

for j in range(trials):
    d=0
    t=0
    for i in range(iter_t):
        r1=random()
        tau=(1/(kfor+kback+kdetach))*log(1/r1)
        t+=tau
        r2=random()
        if r2<kfor/(kfor+kback+kdetach):
            d+=1
        elif r2>=kfor/(kfor+kback+kdetach) and r2<(kback+kfor)/(kfor+kback+kdetach):
            d=d-1
        else:
            break
        dis[i,j]=d
        time[i,j]=t
    D.append(d)


print('average distace =',sum(D)/trials)
print('(kfor-kback)/gamma =',(kfor-kback)/kdetach)
#print(time[0:10,1],dis[0:10,1])
plt.scatter(time[0:20,1],dis[0:20,1])
plt.plot(time[0:20,1],dis[0:20,1], 'r--')
#plt.scatter(time[0:20,2],dis[0:20,2], marker='*')
#plt.plot(time[0:20,2],dis[0:20,2], 'g--)
plt.show()
