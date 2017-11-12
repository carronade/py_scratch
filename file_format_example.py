

import pandas as pd
import time
import h5py
import dask.dataframe as dd
import numpy as np

t0 = time.time()
t = pd.read_csv(r'D:\pairs_data\dailyret_long.csv')
print 'pd.read_csv takes {} sec'.format(time.time()-t0)

# only one data type allowed
t0 = time.time()
with h5py.File('D:\pairs_data\dailyret_long.h5', 'w') as hf:
    hf.create_dataset('dailyret_long', data=t[['Date', 'ret']], dtype=np.float)
print 'save DF to h5 takes {} sec'.format(time.time()-t0)

# obtained data is np.ndarray...
t0 = time.time()
with h5py.File('D:\pairs_data\dailyret_long.h5', 'r') as hf:
    t2 = hf['dailyret_long'][:]
print 'read DF from h5 takes {} sec'.format(time.time() - t0)

# This uses pandas\io\pytables.py
# doesn't work
# t0 = time.time()
# with pd.HDFStore('D:\pairs_data\dailyret_long1.h5') as hf:
#     hf.put('d1', t[['Date', 'ret']], format='table')
#     print 'save DF to h5 takes {} sec'.format(time.time() - t0)

t0 = time.time()
t = dd.read_csv(r'D:\pairs_data\dailyret_long.csv')
print 'dd.read_csv takes {} sec'.format(time.time()-t0)


