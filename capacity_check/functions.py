# ............... IMPORTS
# import sparse module from SciPy package
from scipy import sparse
# import uniform module to create random numbers
from scipy.stats import uniform
# import NumPy
import numpy as np
# import matplotlib
import matplotlib as mpl


# ............... SIGMOID
def sigmoid(x,g)
    sigm = 1./(1+np.exp(-g*x))
    return sigm

# ...............
