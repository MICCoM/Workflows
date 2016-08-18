
# Bonds Dummy
# Dummy scripts for Bonds workflow

# Global variables
state = None
# End global variables

import random
import sys

class BondState:

    """ All science functionality is in the class. """
    
    def __init__(self):
        """ Pretend to initialize something"""
        print("BondState.init() ...")

    def sim(self, step, sample, cuts):
        """ Args: 
                 cuts (list): the cuts to apply
            Returns: a pretend energy level, 
                 which is a function of the step, sample, and cuts
        """
        print("BondState.sim(%s) ..." % cuts)
        energy = 1000 - (step+sample+random.randint(0,10)+sum(cuts))
        print("BondState.sim energy: " + str(energy))
        return energy

    def select_cut(self, cut_list):
        """ Args: A list of pairs generated by sim()
            Returns: The best cut list
        """
        lowest_energy = sys.maxint
        best_cuts = None
        for c in cut_list:
            if c[0] < lowest_energy:
                lowest_energy = c[0]
                best_cuts = c[1]
        print("selected: energy: %i cuts: %s" %
              (lowest_energy, str(best_cuts)))
        return best_cuts

# Swift interface functions:
# obtain simple data types from Swift,
# unpack and pass into science code,
# pack and return to Swift via repr()
    
def sim(step, sample, cuts):
    global state
    if state == None:
        state = BondState()
    c = eval(cuts)
    print("sim: step: %i sample: %i cuts: %s" % (step, sample, str(c)))
    energy = state.sim(step, sample, c)
    result = [ energy, c+[sample] ]
    return repr(result)

def select_cut(cut_list):
    global state
    C = eval(cut_list)
    L = []
    L.extend(C)
    result = state.select_cut(L)
    return repr(result)
