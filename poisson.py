# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 15:27:45 2019

@author: Liu Yang
"""

from scipy.stats import poisson
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')

lamda=[2,6,10,20]
ps=[poisson(i) for i in lamda]
x=np.arange(30)
fig, ax = plt.subplots(nrows=1,ncols=2,figsize=(8,5))
for i in lamda: 
    ax[0].plot(x,poisson.pmf(x,i),label='lamda='+str(i))
    ax[1].plot(x,poisson.cdf(x,i),label='lamda='+str(i))
ax[0].set_xlabel('x')
ax[1].set_xlabel('x')
ax[0].set_ylabel('pmf')
ax[1].set_ylabel('cdf')
ax[0].legend(loc='best')
ax[1].legend(loc='best')
fig.suptitle('Poisson distribution')
#fig.tight_layout()
fig.savefig(r'C:\Users\10245\Desktop\数学笔记\泊松分布参数lamda的检验\poisson.png',dpi=300)
plt.show()

