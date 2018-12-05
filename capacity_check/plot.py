import matplotlib.pyplot as plt
import numpy as np
dades = []
i = 0
with open("dades.txt", 'r') as fitxer:
    for line in fitxer:
        dades.append([])
        dades[i] = [int(n) for n in line.split('\t')]
        i += 1
dades_so = []
j = 0
with open("dades_suboptimal.txt", 'r') as fitxer_so:
    for line in fitxer_so:
        dades_so.append([])
        dades_so[j] = [int(n) for n in line.split('\t')]
        j += 1

# fitxer = open("dades.txt", 'r')
# dades_llegir = fitxer.read()
# dades = dades_llegir.split()

#print dades
resultats = np.zeros([6, 2])
resultats_so = np.zeros([6, 2])
for i in range(6):
    dum = np.zeros(10)
    dum_so = np.zeros(10)
    for j in range(10):
        # print dades[i*10+j][0], dades[i*10+j][1]
        dum[j] = dades[i*10+j][1]
        dum_so[j] = dades_so[i*10+j][1]
    resultats[i][0] = dum.mean()
    resultats[i][1] = dum.std()
    resultats_so[i][0] = dum_so.mean()
    resultats_so[i][1] = dum_so.std()

print resultats[:, 1], range(100, 600, 100)
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


nrange = [100, 200, 300, 400, 500, 1000]
plt.errorbar(nrange, resultats[:, 0], yerr=resultats[:, 1], fmt='o', color='r', label='Simulation w/ optimal parameters')
plt.errorbar(nrange, resultats_so[:, 0], yerr=resultats_so[:, 1], fmt='o', color='b', label='Simulation w/ 3x optimal q_')
frange = range(100, 1000, 1)
plt.plot(frange, finitesize(frange), color='k', label='Prediction w/ finite size effects')
plt.axis([90,1010,0,150])
ax = plt.gca()
ax.legend(loc='upper left')
ax.set_xlabel('N')
ax.set_ylabel('P')
# ax.set_yscale('log', nonposy='clip')
plt.show()
