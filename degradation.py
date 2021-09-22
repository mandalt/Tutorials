#degradation of a single chemical species
import numpy as np
import matplotlib.pyplot as plt
from random import random 
from math import log
 
k=0.1 #rate of degradation
a=np.zeros((20,11))
avg=[]

for i in range(1,11):
    A0=20 #initial concentration
    t=0
    A=[]
    tstep=[]
    while A0>0:
        r=random()
        tau=(1/A0*k)*log(1/r)
        t+=tau
        A0-=1
        A.append(A0)
        tstep.append(t)
    a[:,0]=A
    a[:,i]=tstep
    plt.step(a[:,i],a[:,0])
    plt.axis((0,0.8,0,20))
    
for i in range(20):
    avg.append(sum(a[i,1:11])/10.)
plt.plot(avg,a[:,0], color='k')
plt.title("degradation of A")
plt.xlabel("time")
plt.ylabel("no. of A")
#plt.show()
plt.savefig("degradation.png")#degradation of a single chemical species

