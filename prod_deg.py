#production and degradation
import numpy as np
import matplotlib.pyplot as plt
from random import random 
from math import log, factorial, exp
 
kdeg=0.1 #rate of degradation
kprod=1. #rate of production
iter_t=10000
avgA=[]
avgT=[]
a=np.zeros((iter_t,1000))
time=np.zeros((iter_t,1000))
z=[]

for i in range(1000):
    A0=0
    t=0
    A=[]
    tstep=[]
    for j in range(iter_t):
        r1=random()
        tau=(1/(A0*kdeg+kprod))*log(1/r1)
        t+=tau
        r2=random()
        if r2<kprod/(A0*kdeg+kprod):
            A0+=1
        else:
            A0-=1
        A.append(A0)
        tstep.append(t)    
    a[:,i]=A
    time[:,i]=tstep

plt.step(time[0:100,0:10],a[0:100,0:10])
#print(z)    
for i in range(100):
    avgA.append(sum(a[i,:])/1000.)
    avgT.append(sum(time[i,:])/1000.)
plt.plot(avgT,avgA,color='k')
plt.title("production and degradation of A")
plt.xlabel("time")
plt.ylabel("no. of A")
#plt.show()
plt.savefig("prod&degrad.png")
z=np.append(z,a[50:iter_t,:])#assuming it reaches stationary state after 50 iterations
n=np.arange(0,22,1)
phi=np.zeros(len(n))
for i in range(len(n)):
    phi[i]=(1/factorial(int(n[i])))*((kprod/kdeg)**int(n[i]))*(exp(-kprod/kdeg))
plt.figure()
plt.hist(z,bins=n,density=True)
plt.plot(n,phi)
plt.title("stationary distribution of A and B")
plt.xlabel("count")
plt.xlabel("no. of A")
#plt.show()
plt.savefig("prod&degrad_hist.png")

