import glob
import os
import pandas as pd
path =r'C:\Users\54261\OneDrive\Escritorio\Proyecto-individual I\clientes'
filenames = glob.glob(path + "/*.csv")
dfs = []
for filename in filenames:
    dfs.append(pd.read_csv(filename))

# Concatenate all data into one DataFrame
big_frame = pd.concat(dfs, ignore_index=True)
