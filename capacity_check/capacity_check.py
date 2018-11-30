# ............... IMPORTS
from scipy.sparse import csr_matrix   # import compressed sparse row
from random import sample             # import sample (rnd from a list, no repetition)
from random import randrange          # generate a random number between two integers
from random import shuffle            # random reorganization of an array
#from numpy.ndarray import resize           # reshape an array into another shape
import numpy as np
# ............... File headers
from definitions import N, L, f, q_10, q_01

# ............... Generate patterns
pattern = np.zeros((L, N))  # L rows and N columns matrix to store the patterns
for i in range(L):   # for each of the L memories   TODO eliminate the for loop somehow
    pattern[i][sample(range(int(N)), int(N*f))] = 1  # activate N*f random neurons
# sparse_pattern = csr_matrix(pattern)  # transform the patterns matrix into a sparse matrix

# ............... Generate connectivity matrix
w = np.zeros((N, N)) # connectivity matrix initialized at zero values
# w = np.array([0]*int(N*N*(1-f))+[1]*int(N*N*f)) # create a vector with N*N(1-f) zeros and N*N*f ones
# shuffle(w)  # shuffle it to make it random
# w.resize((N, N))    # resize it to N*N shape

for i in range (L):  # range(L):   # for each of the L memories
    potmat = np.outer(pattern[i][:], pattern[i][:])  # create potentiation matrix from pattern i vector product (qp=1)

    depmat10 = np.outer(pattern[i][:], 1-pattern[i][:])  # create depression matrix from pattern i reversed vector
    depmat10[np.nonzero(depmat10)] *= np.random.rand(f*(1-f)*N**2)  # multiply non zeros by random number
    depmat10[depmat10>=q_10] = 0                         # erase all randoms higher than q_10
    depmat10[0<depmat10] = 1                      # turn to events all randoms lower than q_10

    depmat01 = np.outer(1-pattern[i][:], pattern[i][:])  # create depression matrix from pattern i reversed vector
    depmat01[np.nonzero(depmat01)] *= np.random.rand(f*(1-f)*N**2)  # multiply non zeros by random number
    depmat01[depmat01>q_01] = 0                         # erase all randoms higher than q_10
    depmat01[0<depmat01<=q_01] = 1                      # turn to events all randoms lower than q_10

    potdep = potmat-depmat10-depmat01
w += potdep
np.clip(w, 0, 1)

print w

