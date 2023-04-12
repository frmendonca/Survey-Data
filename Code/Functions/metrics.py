import numpy as np

def compute_metrics(table):

    # SHEC
    SEHC = np.sum(np.diag(table))/np.sum(table)

    # Liu Lu measure
    Mm = table.sum(axis = 1)
    Fm = table.sum(axis = 0)
    N = table.sum()

    Qm = np.floor(Mm[-1]*Fm[-1]/N)
    LL = (table[1,1] - Qm)/(min(Mm[-1], Fm[-1]) - Qm)

    return {'SEHC': SEHC, 'LiuLu': LL}

