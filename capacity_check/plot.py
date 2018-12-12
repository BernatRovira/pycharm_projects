#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
dades_o = []
i = 0
with open("dades.txt", 'r') as fitxer:
    for line in fitxer:
        dades_o.append([])
        dades_o[i] = [int(n) for n in line.split('\t')]
        i += 1
dades_so = []
j = 0
with open("dades_suboptimal.txt", 'r') as fitxer_so:
    for line_so in fitxer_so:
        dades_so.append([])
        dades_so[j] = [int(n) for n in line_so.split('\t')]
        j += 1
dades_fix = []
k = 0
with open("dades_fixed.txt", 'r') as fitxer_fix:
    for line_fix in fitxer_fix:
        dades_fix.append([])
        dades_fix[k] = [int(n) for n in line_fix.split('\t')]
        k += 1


# fitxer = open("dades.txt", 'r')
# dades_llegir = fitxer.read()
# dades = dades_llegir.split()

#print dades
# resultats = np.zeros([10, 2])     # OLD WAY OF PERFORMING MEANS, UNADAPTABLE
# resultats_so = np.zeros([10, 2])
# for i in range(10):
#    dum = np.zeros(10)
#    dum_so = np.zeros(10)
#     for j in range(10):
#        # print dades[i*10+j][0], dades[i*10+j][1]
#         dum[j] = dades[i*10+j][1]
#         dum_so[j] = dades_so[i*10+j][1]
#     resultats[i][0] = dum.mean()
#     resultats[i][1] = dum.std()
#     resultats_so[i][0] = dum_so.mean()
#     resultats_so[i][1] = dum_so.std()

resultats_o = []               # ADAPTABLE NEW WAY OF PERFORMING MEAN AND STD
index_o = 0
while index_o < len(dades_o):   # while we haven't run over all dades
    dum_o = []     # empty array as the base for the means etc 
    d0m_o = dades_o[index_o][0]     #  for index is the first element
    while dades_o[index_o][0] == d0m_o:   # while dades[index] first elem is i*100
        dum_o.append(dades_o[index_o][1])    # append the second elem to dum
        index_o += 1   # and update the index
        if index_o==len(dades_o): # if the index is at dades length -1
            break
    print index_o
    resultats_o.append([np.asarray(dum_o).mean(), np.asarray(dum_o).std()])

resultats_so = []
index_so = 0
while index_so < len(dades_so):   # while we haven't run over all dades
    dum_so = []     # empty array as the base for the means etc 
    d0m_so = dades_so[index_so][0]     #  for index is the first element
    while dades_so[index_so][0] == d0m_so:   # while dades[index] first elem is i*100
        dum_so.append(dades_so[index_so][1])    # append the second elem to dum
        index_so += 1   # and update the index
        if index_so==len(dades_so): # if the index is at dades length -1
            break
    print index_so
    resultats_so.append([np.asarray(dum_so).mean(), np.asarray(dum_so).std()])

resultats_fix = []
index_fix = 0
while index_fix < len(dades_fix):   # while we haven't run over all dades
    dum_fix = []     # empty array as the base for the means etc 
    d0m_fix = dades_fix[index_fix][0]     #  for index is the first element
    while dades_fix[index_fix][0] == d0m_fix:   # while dades[index] first elem is i*100
        dum_fix.append(dades_fix[index_fix][1])    # append the second elem to dum
        index_fix += 1   # and update the index
        if index_fix==len(dades_fix): # if the index is at dades length -1
            break
    print index_fix
    resultats_fix.append([np.asarray(dum_fix).mean(), np.asarray(dum_fix).std()])



def f(N):
    return beta*np.log(N)/N
def q_(f):
    return 2.57*f/(1-f)   # depression probability
beta = 2.44
theta = 0.72
g = 0.28
def finitesize(N):
    c1 = (g/(beta**2))*np.log((1-g)/(theta-g))
    c2 = np.sqrt(theta*(1-theta))/(np.sqrt(beta)*(theta-g)*np.log((1-g)/(theta-g)))
    P = c1*((N/np.log(N))**2)*(1 - c2 * np.sqrt(np.log(np.log(N)) / np.log(N)))
    return P

nrange_o = 100*np.arange(1,len(resultats_o)+1)
plt.errorbar(nrange_o, np.asarray(resultats_o)[:, 0], yerr=np.asarray(resultats_o)[:, 1], fmt='o', color='r', label='Simulation w/ optimal f, q_')

nrange_so = 100*np.arange(1,len(resultats_so)+1)
plt.errorbar(nrange_so, np.asarray(resultats_so)[:, 0], yerr=np.asarray(resultats_so)[:, 1], fmt='o', color='b', label='Simulation w/ 3x optimal f, q_')

nrange_fix = 100*np.arange(1,len(resultats_fix)+1)
plt.errorbar(nrange_fix, np.asarray(resultats_fix)[:, 0], yerr=np.asarray(resultats_fix)[:, 1], fmt='o', color='g', label='Simulation w/ fixed f, q_')
frange = range(100, 1000, 1)
frange = range(100, 1000, 1)
plt.plot(frange, finitesize(frange), color='k', label='Prediction w/ finite size effects')

print [range(100,1100,100) , resultats_fix]

plt.plot(frange,-25.48+2.2678*np.sqrt(frange), color='k', label='Square root of N (fitted)')
plt.axis([90, 1010, 0, 180])
ax = plt.gca()
ax.legend(loc='upper left')
ax.set_xlabel('N')
ax.set_ylabel('P')
# ax.set_yscale('log', nonposy='clip')
plt.show()
plt.save('figprova', format=pdf)
