from time import time
import timeit
import feather
import numpy as np
import pandas as pd 


def create_dataframe():
    df = pd.DataFrame({
        'row1' : np.random.rand(100000),
        'row2' : np.random.rand(100000),
        'row3' : np.random.rand(100000),
        'row4' : np.random.rand(100000),
    })
    return df

def save_df_2_feather(df):
    df.to_feather('data2.feather')

def save_df_2_csv(df):
    df.to_feather('data.csv')

def read_feather():
    df = pd.read_feather("data2.feather")
    return df

def read_csv():
    df = pd.read_csv("data.csv")
    return df

duration_read_feather =0
duration_read_csv =0
duration_write_feather =0
duration_write_csv =0

start = timeit.default_timer()
save_df_2_feather(df=create_dataframe())
duration_write_feather += timeit.default_timer() - start

start = timeit.default_timer()
save_df_2_csv(df=create_dataframe())
duration_write_csv += timeit.default_timer() - start

start = timeit.default_timer()
df_1= read_feather()
duration_read_feather += timeit.default_timer() - start

start = timeit.default_timer()
df_2=read_csv()
duration_read_csv += timeit.default_timer() - start


print(duration_read_feather)
print(duration_read_csv)
print(duration_write_feather)
print(duration_write_csv)
