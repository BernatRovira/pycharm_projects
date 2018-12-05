import numpy as np
# ............... Model parameters
N = np.float64(9e2)      # Neuron number
beta = 2.44     # parameter for coding level
gama = 100      # sigmoid steepness
theta = 0.0    # Treshold
f = beta*np.log(N)/N     # coding level
qp = 1 # potentiation probability
q_ = 2.57*f/(1-f)   # depression probability
q_01 = q_/2  # depression probability 01
q_10 = q_/2  # depression probability 10
L = np.round(np.log(1e-5)/np.log(1-qp*f**2-f*(1-f)*q_))  # Lsteady eq 2.20 thesis draft
g = 1/(1+(1-f)*q_/f)
gp = g+(1-g)*np.exp(-0.14/g)
w_EI = gp       # inh to exc synaptic weight
t_E = 1.      # Excitatory time constant
t_I = 0.5     # Inhibitory time constant

# ............... Simulation parameters 
dt = 0.1      # Time step
rlzt = 10     # Realizations per iteration
test_n = 150  # Number of patterns to be tested


import time

class CodeTimer:
    def __init__(self, name=None):
        self.name = " '"  + name + "'" if name else ''

    def __enter__(self):
        self.start = time.clock()

    def __exit__(self, exc_type, exc_value, traceback):
        self.took = (time.clock() - self.start) * 1000.0
        print('Code block' + self.name + ' took: ' + str(self.took) + ' ms')
