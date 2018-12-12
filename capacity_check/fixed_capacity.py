#!/usr/bin/env python
# ............... IMPORTS
from scipy.sparse import csr_matrix   # import compressed sparse row
from random import sample             # import sample (rnd from a list, no repetition)
# from random import shuffle            # random reorganization of an array
import numpy as np
# import matplotlib.pyplot as plt
# from definitions import CodeTimer

import sys  # to pass arguments to the script

# ............... Model parameters
N = float(sys.argv[1])  # N is the first argument (argv[0] is filename)
q_ = float(sys.argv[2])  # q_: depression probability
f = float(sys.argv[3])  # f: coding level
# multiplier = float(sys.argv[2])  # multiplier of q_
# N = np.float64(1e2)      # Neuron number (imported as argument)
beta = 2.44     # parameter for coding level
gama = 100      # sigmoid steepness
theta = 0.0    # Treshold
# f = beta*np.log(N)/N     # coding level
qp = 1  # potentiation probability
# q_ = multiplier*2.57*f/(1-f)   # depression probability
q_01 = q_/2  # depression probability 01
q_10 = q_/2  # depression probability 10
L = np.round(np.log(1e-4)/np.log(1-qp*f**2-f*(1-f)*q_))  # Lsteady eq 2.20 thesis draft
g = 1/(1+(1-f)*q_/f)
gp = g+(1-g)*np.exp(-0.14/g)
w_EI = gp       # inh to exc synaptic weight
t_E = 1.      # Excitatory time constant
t_I = 0.5     # Inhibitory time constant

# ............... Simulation parameters
dt = 0.1      # Time step
rlzt = 10     # Realizations per iteration

#  from definitions import L, f, q_, q_10, q_01, g, gp

n_test = int(np.round(np.log(1e-3)/np.log(1-qp*f**2-f*(1-f)*q_))) # Lsteady eq 2.20 thesis draft
print N, L, n_test
# print L, int(N*(1.-f)), int(N*f), np.ceil(N*(1-f)), 16*984
# raw_input('debugger')


# ............... Generate patterns
pattern = np.zeros((L, N))  # L rows and N columns matrix to store the patterns
for i in range(int(L)):   # for each of the L memories   TODO eliminate the for loop somehow
    pattern[i][sample(range(int(N)), int(N*f))] = 1  # activate N*f random neurons
sparse_pattern = csr_matrix(pattern)  # transform the patterns matrix into a sparse matrix

# ............... Generate connectivity matrix
n_ones_depmat = int(N*f)*np.ceil(N*(1.-f))  # number of ones in the depression matrix
w_evo = np.zeros(L)   # evolution of weight matrix started at zero also
w_steady = 1/(1+(1-f)*q_/(f-1/N))  # expected avg value of steady w, accounting for small N
w = np.zeros((int(N), int(N)))  # connectivity matrix initialized at zero values
# w = np.array([0]*int(N*N*(1-w_steady))+[1]*np.round(N*N*w_steady))  # vector with N^2*w_steady ones
# shuffle(w)  # shuffle it to make it random
# w.resize((N, N))    # resize it to N*N shape


for i in range(int(L)):  # range(L):   # for each of the L memories
    if (i % 100) == 0:
        print i

    # with CodeTimer('potmat'):
    potmat = np.outer(pattern[i][:], pattern[i][:])  # create pot matrix from pattern i vector product (qp=1)

    # with CodeTimer('depmat10'):
    depmat10 = np.outer(pattern[i][:], 1-pattern[i][:])  # create depression matrix from pattern i reversed vector
    # rndvec = np.random.rand(n_ones_depmat)  # generate as many rnd as ones in the matrix
    # rndvec[np.where(rndvec < q_10)] = 1     # set the rnd below prob to one (they will modify)
    # np.floor(rndvec, rndvec)                        # and the rest to zero (they will not modify)
    # depmat10[np.where(depmat10 > 0)] *= rndvec  # multiply non zeros by random number
    rndvec = (np.random.rand(n_ones_depmat) < q_10)
    depmat10[depmat10 > 0] = depmat10[depmat10 > 0]*rndvec

    # with CodeTimer('depmat01'):
    depmat01 = np.outer(1-pattern[i][:], pattern[i][:])  # create depression matrix from pattern i reversed vector
    # rndvec[np.where(rndvec < q_01)] = 1     # set the rnd below prob to one (they will modify)
    # np.floor(rndvec, rndvec)                        # and the rest to zero (they will not modify)
    # depmat01[np.where(depmat01 > 0)] *= rndvec  # multiply non zeros by random number
    rndvec2 = (np.random.rand(n_ones_depmat) < q_01)
    depmat01[depmat01 > 0] = depmat01[depmat01 > 0]*rndvec2

    # print i, depmat10.sum(), depmat01.sum()
    # with CodeTimer('weight updating'):
    w = np.clip(w+potmat-depmat10-depmat01, 0, 1)  # apply synapse modifications and clip to boundaries
    # w[potmat > 0] += potmat[potmat > 0]   # alternative method, slower
    # w[depmat10 > 0] -= depmat10[depmat10 > 0]
    # w[depmat01 > 0] -= depmat01[depmat01 > 0]
    # w[w != 0] = np.clip(w[w != 0], 0, 1)
    # w = w+potmat-depmat10-depmat01        # another one, also slower
    # w[w>1] = 1
    # w[w<0] = 0

    # with CodeTimer('weight counting'):
    # w_evo[i] = np.count_nonzero(w)                 # count nonzero elements to record w evolution
sparse_w = csr_matrix(w)

# plt.plot(w_evo)
# plt.axhline(y=N*N*w_steady, color='r', linestyle='-')
# plt.show()

# ............... Stability testing
# n_test = int(500)
test_result = np.zeros(n_test)
for i in range(int(L)-n_test, int(L)):  # for each pattern
    state = w.dot(pattern[i][:].T)      # compute w_ij*r_j
    mask_state = state > N*f*gp         # mask to the inh value
    if np.all(mask_state == pattern[i][:]):  # if the mask coincides with the pattern
        test_result[i-int(L)+n_test] += 1  # check the pattern as 1 (stable)
fitxer = open("dades_fixed.txt", "a")
fitxer.write("%d\t%d\n" % (N, test_result.sum()))
