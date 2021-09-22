#kinesin walking on microtubule

import numpy as np
import matplotlib.pyplot as plt
from random import random
from math import log

kfor=1.       #rate of taking a step forward
kdetach=0.8   #rate of getting detached
iter_t=1000
trials=10000
D=[]

for j in range(trials):
    d=0
    t=0
    for i in range(iter_t):
        r1=random()
        tau=(1/(kfor+kdetach))*log(1/r1)
        t+=tau
        r2=random()
        if r2<kfor/(kfor+kdetach):
            d+=1
        else:
            break
    D.append(d)
    
print('average distace =',sum(D)/trials)
print('k+/gamma =', kfor/kdetach)
