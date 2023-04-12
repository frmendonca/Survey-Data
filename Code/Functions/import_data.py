

import numpy as np
import pandas as pd


PATH = r'C:\Users\franc\OneDrive\Documentos\Projetos\Artigos\Survey Data\Data\US_IPUMS_Census.xlsx'
K = 6

def import_dataset():

    xl = pd.ExcelFile(PATH)
    res = len(xl.sheet_names)

    data = [np.asarray(pd.read_excel(PATH, sheet_name = x, header=None)) for x in xl.sheet_names]
    
    return data

