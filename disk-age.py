#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 11:28:34 2023

@author: mac
"""

#figsize
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splrep,splev,splint
import csv

DATA,X,Y = [],[],[]
csvFile = open('data.csv', "r")
dict_reader = csv.DictReader(csvFile)
for row in dict_reader:
    DATA.append(row)
for i in range(len(DATA)):
    X.append(float(DATA[i]['alpha']))
    Y.append(float(DATA[i]['Y']))
tck_36 = splrep(X,Y,k=3,s=0.08)

alpha_min,alpha_max = -3.0694440059544545,4.814672904812319

Total_lifetime = splint(alpha_max,alpha_min,tck_36)*2/splint(-1.6,-0.3,tck_36)
Age_negative_list = []
alpha_list = np.linspace(alpha_min,alpha_max,500)
for i in alpha_list:
    Age_negative_list.append(splint(alpha_max,i,tck_36)*Total_lifetime/splint(alpha_max,alpha_min,tck_36))

Y_36 = splev(alpha_list,tck_36)

h_fig,w_fig = 2,1
panel_size = 6
fig = plt.figure(figsize=(w_fig * panel_size ,h_fig * panel_size))
ax1 = fig.add_subplot(h_fig,w_fig,1)
ax1.step(X,Y,where='mid',c='k',label='36 sub-regions',
        zorder=2)
ax1.plot(alpha_list,Y_36,'k--',zorder=2)

ax1.set_xlabel(r'$\alpha$',fontsize = 15)
ax1.tick_params(axis='both',labelsize=15,colors='k')
ax1.grid(False)
ax1.legend(fontsize=15)
ax1.minorticks_on()

ax1.tick_params(axis='both',which='both',colors='k',
               top='on',bottom='on',left='on',right='on',
               direction='in')

ax2 = fig.add_subplot(h_fig,w_fig,2)
ax2.plot(alpha_list,Age_negative_list,c='k',)
ax2.tick_params(axis='both',which='both',colors='k',
                top='on',bottom='on',left='on',right='on',
                direction='in',  )
ax2.set_xlabel(r'$\alpha$',fontsize=15)
ax2.set_ylabel(u"-Age(Myr)",fontsize=15)
ax2.tick_params(axis='both',labelsize=15,colors='k')
ax2.minorticks_on()
ax2.vlines(x=-2,ymin=-3.1,ymax=0,colors="gray", ls="--", lw=1, )
plt.savefig('alpha-age.png',bbox_inches = 'tight')
plt.show()



def Age_negative(alpha,alpha_min,alpha_max,tck_36,Total_lifetime):
    Age_negative = splint(alpha_max,alpha,tck_36)*Total_lifetime/splint(alpha_max,alpha_min,tck_36)
    return Age_negative



#Input a value on alpha position in Age_negative function, you can get the corresponding disk-age.
print(Age_negative(0,alpha_min,alpha_max,tck_36,Total_lifetime))













