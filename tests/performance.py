import numpy as np
import random
import pandas as pd
from khash.hashtable import Int64HashTable, StringHashTable, Float64HashTable

def new_klib_int(input_array):
    ht = Int64HashTable(len(input_array))
    return ht.get_labels_groupby(input_array)

def new_klib_str(input_array):
    ht = StringHashTable(len(input_array))
    return ht.factorize(input_array)

def new_klib_float(input_array):
    ht = Float64HashTable(len(input_array))
    return ht.factorize(input_array)

# a = np.random.randint(100, size=10000000)
# b = np.fromiter((random.choice(['NY', 'IL', 'OH', 'CA']) for _ in xrange(10000000)), dtype='S2')
# b = pd.Series(b).values
# c = np.random.random_sample(10000000) * 10000

# %timeit pd.factorize(a)
# %timeit new_klib_int(a)
# %timeit pd.factorize(b)
# %timeit new_klib_str(b)
# %timeit pd.factorize(c)
# %timeit new_klib_float(c)

# In [20]: %timeit pd.factorize(a)
# 10 loops, best of 3: 122 ms per loop
#
# In [21]: %timeit new_klib_int(a)
# 10 loops, best of 3: 101 ms per loop
#
# In [22]: %timeit pd.factorize(b)
# 1 loops, best of 3: 496 ms per loop
#
# In [23]: %timeit new_klib_str(b)
# 10 loops, best of 3: 165 ms per loop
#
# In [36]: %timeit pd.factorize(c)
# 1 loops, best of 3: 1.61 s per loop
#
# In [37]: %timeit new_klib_float(c)
# 1 loops, best of 3: 1.44 s per loop
#
