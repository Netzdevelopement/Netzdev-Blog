import feather
import numpy as np
import pandas as pd 

df = pd.DataFrame({
    'row1' : np.random.rand(100000),
    'row2' : np.random.rand(100000),
    'row3' : np.random.rand(100000),
    'row4' : np.random.rand(100000),
})

df.to_feather('data.feather')