import pandas as pd
import numpy as np

# mL/frameworks/pandas/operations/csv_converters
# # Load csv to pandas
df = pd.read_csv('/home/vince/Desktop/youthy.csv')
print(df)
# # convert csv to matrix
matrix = df.as_matrix()
print(matrix)

# # df.replace
df2 = df.replace(to_replace=[19, 'cobbs', 'no'], value=0)
df3 = df2.replace(to_replace=[17, 18, 'cedar', 'yes'], value=1)
print(df3)

# # NumPy converters
# # # > create DataFrame from numpy array
# array = np.ones(shape=(3, 3))
# df = pd.DataFrame(data=array)
# print(df)


