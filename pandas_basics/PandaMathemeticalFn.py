import pandas as pd
import numpy as np

# Pandas Dataframe is two-dimensional size-mutable, potentially heterogeneous tabular data structure with labeled axes (rows and columns).
df_random = pd.DataFrame(np.random.rand(10,5))
#remember shape is (10,5) not 10,5
df_ones = pd.DataFrame(np.ones((10,5)))
df_zeros = pd.DataFrame(np.zeros((10,5)))

#Pandas Series is One-dimensional ndarray with axis labels
#Series does not have second dimension i.e shape is (10,)
sr_ones_col = pd.Series(np.ones(10))
sr_ones_row = pd.Series(np.ones(5))
sr_zeros_col = pd.Series(np.zeros(10))
sr_zeros_row = pd.Series(np.zeros(5))

#Mathematical operations
df_sum = df_random + df_ones
#uses broadcasting along rows
df_sum_br = df_ones + sr_ones_row
#due to less size (5<10) of actual table other values get as NaN
df_sum_br_= df_ones + sr_ones_col

#Mathematical operations

df_prod = df_random * df_zeros
#uses broadcasting along rows
df_prod_br = df_ones * sr_zeros_row
#due to less size (5<10) of actual table other values get as NaN
df_prod_br = df_ones * sr_ones_col
df_pow_br = df_random ** df_zeros

#important functions
df_mean = df_random.mean(axis=0)
df_mean = df_random.mean(axis=1)
df_max = df_random.max()
df_min = df_random.min()
df_cum = df_random.cummax()
df_median =  df_random.median()
df_mod = df_random.mode()
df_std = df_random.std()
df_sum_0 = df_random.sum() # vertical direction
df_sum_1 = df_random.sum(axis=1) # ----> horizontal direction

df_sum = df_random.add(df_ones)
df_sub = df_random.subtract(df_ones)
df_prod = df_random.mul(df_zeros)
df_div = df_random.div(df_ones)
df_mod = df_random.mod(df_ones)
df_pow = df_random.pow(df_zeros)
df_eq = df_ones.eq(df_zeros)

#(10,5)*(5,1) = (10,1)
df_dot = df_ones.dot(sr_ones_row)
#not compatible size
#print df_ones.dot(df_random)  #throws error
print df_dot
print df_sum