# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 17:35:59 2019

@author: Liu Yang
"""

import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')

def accumulation(n,p,c,size=10000):
    result=0
    size_float=float(size)
    for i in range(c+1):
        result+=sum(np.random.binomial(n,p,size=size)==i)/size_float        
    return result

n1=100
n2=30
s1=[]
s2=[]
c1=15
c2=25
p=np.arange(0.1,1,0.1)
for ptemp in p:
    s1.append(accumulation(n1,ptemp,c1))
    s2.append(accumulation(n2,ptemp,c1))

fig, ax = plt.subplots(nrows=1,ncols=1,figsize=(7,5))
ax.plot(p,s1,label='n=100')
ax.plot(p,s2,label='n=30')
ax.legend(loc='best')
ax.set_xlabel('Parameter p')
ax.set_ylabel('Cumulative probability of no more than 20 successes')
fig.suptitle('Cumulative probability dicreases when p increases')
fig.savefig(r'C:\Users\10245\Desktop\数学笔记\二项分布参数的检验\binomial_parameter.png',dpi=300)
plt.show()

