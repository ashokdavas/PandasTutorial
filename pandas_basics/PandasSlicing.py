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
#
# #add prefix and suffix to column lables.
df_zeros_prefix = df_zeros.add_prefix('this')

# # #changes the row lables
print df_zeros.rename({0:'first'},inplace=True)
# print df_zeros.loc['first']
#
# print df_random[0]
# print df_random[[0,1]]
# print df_random.loc[:,[0,1]]
# print df_random.iloc[:,[0,1]]
# print df_random.ix[:,[0,1]]
# print df_random.loc[:,0:1]
# print df_random.iloc[:,0:2]
# print df_random.ix[:,0:1]

# #searches for columns with string names
# print df_zeros_prefix.loc[:,'this0':'this1']
# # 'loc' is label based search as there is no label in col with 0:1. so it fails
# # print df_zeros_prefix.loc[0:5,0:1] # will fail
#
# print df_zeros_prefix.iloc[0:5,0:1] # succeed as 'iloc' posititonal
# # print df_zeros_prefix.iloc[:,'this0':'this1'] #will fail. as 'iloc' will not look for labels
#
# print df_zeros_prefix.ix[0:5,0:1] #will exclude 1
# print df_zeros_prefix.ix[:,'this0':'this1'] # will include 'this1'

# # print df_zeros.ix['first':3,0:1]  # not supported
# print df_zeros.ix['first':,0:1]   # supported
#
print df_zeros.loc['first':,0:1] #supported
# # print df_zeros.loc['first':3,0:1] # not supported



