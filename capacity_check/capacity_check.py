# ............... IMPORTS
from scipy.sparse import csr_matrix   # import compressed sparse row
from random import sample             # import sample (rnd from a list, no repetition)
from random import shuffle            # random reorganization of an array
#from numpy.ndarray import resize           # reshape an array into another shape
import numpy as np
# ............... File headers
from definitions import N, L, f

# ............... Generate patterns
pattern = np.zeros((L, N))  # L rows and N columns matrix to store the patterns
for i in range(L):   # for each of the L memories   TODO eliminate the for loop somehow
    pattern[i][sample(range(int(N)), int(N*f))] = 1  # activate N*f random neurons
sparse_pattern = csr_matrix(pattern)  # transform the patterns matrix into a sparse matrix

# ............... Generate connectivity matrix
#w = np.zeros((N, N)) # connectivity matrix initialized at zero values
w = np.array([0]*int(N*N*(1-f))+[1]*int(N*N*f)) # create a vector with N*N(1-f) zeros and N*N*f ones
shuffle(w)  # shuffle it to make it random
w.resize((N, N))    # resize it to N*N shape

#for i in range(L):   # for each of the L memories
#    potmat = np.outer(pattern[i][:], pattern[i][:])  # create potentiation matrix from pattern i vector product
#    depmat_10 = np.outer(pattern[i][:], 1-pattern[i][:])  # create depression matrix 10 from i and 1-i
#    depmat_01 = np.outer(1-pattern[i][:], pattern[i][:])  # create depression matrix 01 from i and 1-i



