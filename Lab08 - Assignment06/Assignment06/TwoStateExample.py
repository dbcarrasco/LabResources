"""
Demonstrate use of the TwoStateMarkovChain class.

Modified for BDA18 2018-03-23 by Tom Loredo
"""

import numpy as np
import scipy
import matplotlib as mpl
from matplotlib.pyplot import *
from scipy import *
from scipy import stats

# try:
#     import myplot
# except ImportError:
#     pass

from two_state_markov import TwoStateMarkovChain


ion()


# Define two initializers --- samplers for the starting state.

def init_at_0():
    """
    Initial state sampler returning state 0.
    """
    return 0

# Distribution for a random initial state:
init_half = stats.binom(1, .5).rvs


# Instantiate a chain generator.
tsmc = TwoStateMarkovChain(.07, .03)


n_paths = 10  # number of sample paths to generate


# Simulate paths of length 30, all starting at 0.
tsmc.sim_paths(n_paths, init_at_0, 30)
tsmc.plot_evol(alpha_trace=.1)


# Simulate paths of length 30, starting randomly (p = 1/2).
tsmc.sim_paths(n_paths, init_half, 30)
tsmc.plot_evol(alpha_trace=.1)
