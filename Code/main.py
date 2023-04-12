
import numpy as np
import pandas as pd

from Code.Functions.import_data import import_dataset # Import data
from Code.Functions.table_manipulation import colapse_table # Transform into 2x2 contingency 
from Code.Functions.metrics import compute_metrics # Obtain metrics for 2x2 tables
from Code.Functions.compute_counterfactuals import compute_counterfactual # Compute counterfactuals

import matplotlib.pyplot as plt


data = import_dataset()
data_2 = colapse_table(data)
metrics_contingency = [compute_metrics(x) for x in data_2]

counterfactuals = [compute_counterfactual(data_2[0], data_2[i]) for i in range(len(data_2))]
metrics_counterfactuals = [compute_metrics(x) for x in counterfactuals]


sehc_c = [x['SEHC'] for x in metrics_counterfactuals]
ll_c = [x['LiuLu'] for x in metrics_counterfactuals]


sehc = [x['SEHC'] for x in metrics_contingency]
ll = [x['LiuLu'] for x in metrics_contingency]


plt.plot(sehc_c)
plt.plot(sehc)
plt.show()