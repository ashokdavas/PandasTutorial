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

#Usage of parameters

#Return a tuple representing the dimensionality of the DataFrame.
sr_shape = sr_ones_col.shape #(10,)
df_shape = df_random.shape #(10,5)

#Rows index to use for resulting frame. Will default to np.arange(n) if no indexing information part of input data and no index provided
row_lables = df_random.index

# Column labels to use for resulting frame. Will default to np.arange(n) if no column labels are provided
column_lables = df_random.columns

# dtypes: column wise data type used
df_dtype = df_random.dtypes

#Usage of basic methods

#show first 5 rows in data
df_head = df_random.head()
#show last n(default 5) rows in data
df_tail = df_random.tail(3)

#Generate various summary statistics, excluding NaN values on numerical data such as count,mean,std etc.
#Statistic generated is on the column
desc = df_random.describe()

#drop behavior
#drop rows with label 1 as row is the default axis
df_drop_row = df_random.drop(1)

#drop column with label = 1 by assigning axis = 1;
df_drop_col = df_random.drop(1,1)
df_drop_col = df_random.drop(labels=1,axis=1,level=None,inplace=False,errors='raise')

# DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
#Return object with labels on given axis omitted where alternately any or all of the data are missing
df_drop_na = df_random.dropna(axis=1)

#append to last. indexes are retained if ignore_index=Fales which is default
df_append = df_random.append(other=df_zeros,ignore_index=True)
#can only append a series if ignore_index = True
df_append_s = df_zeros.append(sr_ones_row,ignore_index=True)

# #add prefix and suffix to column lables.
df_zeros_prefix = df_zeros.add_prefix('this')
print df_zeros.add_suffix('this')

# print df_zeros.rename({0:'first'},inplace=True)