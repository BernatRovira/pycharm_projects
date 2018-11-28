# ............... IMPORTS
from scipy.sparse import csr_matrix   # import compressed sparse row
from random import sample             # import sample (rnd from a list, no repetition)
from numpy.random import randint      # import randint (rnd matrix)
from numpy import zeros               # import zeros (zeros matrix)

# ............... File headers
from definitions import N, L, f

# ............... Generate patterns
pattern = zeros((L, N)) # L rows and N columns matrix to store the patterns
for i in range(L):   # for each of the L memories   TODO eliminate the for loop somehow
    pattern[i][sample(range(int(N)), int(N*f))] = 1  # activate N*f random neurons
sparse_pattern = csr_matrix(pattern)  # transform the patterns matrix

# ............... Generate connectivity matrix
w = randint(2, size=(N, N))  # N*N matrix of rnd 0 and 1 -> PROBABILITY 1/2 TODO custom probability
for i in range(L):   # for each of the L memories

