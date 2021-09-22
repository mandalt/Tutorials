#generalised Gillespie algorithm for 2 chemical species
import numpy as np
import matplotlib.pyplot as plt
from random import random 
from math import log, factorial,exp


kaprod=1.2 #rate of degradation
kaa=0.001 #rate of production
kab=0.01
kbprod=1.
iter_t=10000
avgA=[]
avgB=[]
avgT=[]
a=np.zeros((iter_t,10))
b=np.zeros((iter_t,10))
time=np.zeros((iter_t,10))
z=[]
y=[]

for i in range(10):
    A0=0
    B0=0
    t=0
    A=[]
    B=[]
    tstep=[]
    for j in range(iter_t):
        r1=random()
        propensity=(A0*(A0-1)*kaa)+kaprod+(A0*B0*kab)+kbprod
        tau=(1./propensity)*log(1/r1)
        t+=tau
        r2=random()
        if r2<(A0*(A0-1)*kaa)/propensity:
            A0-=2
        elif r2<((A0*(A0-1)*kaa)+(A0*B0*kab))/propensity and r2>=(A0*(A0-1)*kaa)/propensity:
            A0-=1
            B0-=1
        elif r2<((A0*(A0-1)*kaa)+(A0*B0*kab)+kaprod)/propensity and r2>=((A0*(A0-1)*kaa)+(A0*B0*kab))/propensity:
            A0+=1
        elif r2>=((A0*(A0-1)*kaa)+(A0*B0*kab)+kaprod)/propensity:
            B0+=1
        A.append(A0)
        B.append(B0)
        tstep.append(t)
    a[:,i]=A
    b[:,i]=B
    time[:,i]=tstep

for i in range(iter_t):
    avgA.append(sum(a[i,:])/10.)
    avgB.append(sum(b[i,:])/10.)
    avgT.append(sum(time[i,:])/10.)    

plt.step(time[0:100,0:10],a[0:100,0:10])
plt.plot(avgT[0:100],avgA[0:100],color='k')
plt.title("only A")
plt.xlabel("time")
plt.ylabel("no. of A")
#plt.show()
plt.savefig("onlyA.png")
plt.figure()
plt.step(time[0:100,0:10],b[0:100,0:10])
plt.plot(avgT[0:100],avgB[0:100],color='k')
plt.title("only B")
plt.xlabel("time")
plt.ylabel("no. of B")
#plt.show()
plt.savefig("onlyB.png")

print(avgA[9000],avgB[9000])
#z=np.histogram2d(a[100:iter_t,5],b[100:iter_t,5],bins=50)
#z=np.vstack((a[100:iter_t,5],np.transpose(b[100:iter_t,5])))
#print(z)
plt.figure()
plt.hist2d(a[50:iter_t,9],b[50:iter_t,9],bins=25)
plt.title("stationary distributuion of A and B")
plt.ylabel("no. of B")
plt.xlabel("no. of A")
#plt.show()
plt.savefig("AB_hist.png")

