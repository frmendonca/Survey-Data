

import numpy as np
from Code.Functions.metrics import compute_metrics

def compute_counterfactual(availability_table, preferences_table):

    K = availability_table.shape[0]

    # Structural availability
    Mm = availability_table.sum(axis = 1)
    Fm = availability_table.sum(axis = 0)
    N = availability_table.sum()

    Qm = np.floor(Mm[1]*Fm[1]/N)
    min_m = min(Mm[1], Fm[1])
    
    # Preferences
    LLp = compute_metrics(preferences_table)['LiuLu']

    # Compute counterfactual
    c_table = np.zeros((K, K))

    c_table[1, 1] = LLp*(min_m - Qm) + Qm
    c_table[0, 1] = Fm[1] - c_table[1, 1]
    c_table[0, 0] = Mm[0] - c_table[0, 1]
    c_table[1, 0] = Fm[0] - c_table[0, 0]

    return c_table
