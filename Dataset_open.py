import os
import pandas as pd


pd.set_option('display.max_columns',None)

df = pd.read_parquet('a_0.parquet', engine='pyarrow')

print(f'shape of dataframe is {df.shape}')
print(df.head())
