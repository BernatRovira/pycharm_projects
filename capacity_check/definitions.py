# ............... Model parameters 
import numpy as np
N = np.float64(1e1)      # Neuron number
L = 10         # number of patterns to relax con. matrix
f = 0.5  # coding level
gama = 1e3   # sigmoid constant
t_E = 1.      # Excitatory time constant
t_I = 0.5     # Inhibitory time constant
t_W = 1.0e2    # Weight time constant
I_E = 0.      # Excitatory constant input
I_I = 0.      # Inhibitory constant input
theta = 0.5   # Treshold

# ............... Simulation parameters 
dt = 0.1      # Time step
rlzt = 10     # Realizations per iteration
test_n = 150  # Number of patterns to be tested