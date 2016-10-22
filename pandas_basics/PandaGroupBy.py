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

df_zeros_prefix = df_zeros.add_prefix('this')

# grouped = obj.groupby(key)
# grouped = obj.groupby(key, axis=1)
# grouped = obj.groupby([key1, key2])
gdf_random = df_zeros_prefix.groupby('this0')

# print gdf_random.size()
# print gdf_random.mean()
# print gdf_random.sum()
# print gdf_random.mean().loc[0,'this0':'this1']

gdf_random = df_ones.groupby(0)
# print gdf_random.sum()
# print gdf_random.count()
# print gdf_random.median()

#gives the group formed using the . here 1 is the name of group
#group name is the value of [row,column] on which it is grouped
# print gdf_random.get_group(1)

gdf_random = df_random.groupby(0)
# print gdf_random.sum()
#
# for c in gdf_random.groups:
#     print c #name of groups

gdf_random = pd.DataFrame(df_random.groupby(0).mean())
print gdf_random
#takes the numerical values and provide the groups whose labels(numerical in this case) are i range
print gdf_random.ix[0.035642:0.458025,0:2]
#ix not perform positional search as labels itself are numerical
print gdf_random.ix[0:2,0:2]

#loc performs the positional search
print gdf_random.iloc[0:2,0:2]