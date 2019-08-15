import pandas as pd
import numpy as np

# construct DataFrame from a dictionary
dictionary = {'column_1': [1, 5], 'column_2': [9, 19]}
df = pd.DataFrame(dictionary)  # default datatype is int64
# or pd.DataFrame(data = d, dtype = np.int8/16/32 etc)
print(df)

# or construct the DataFrame from a numpy array
numpyArray = np.array([[1, 2, 3], [3, 2, 1]])
df = pd.DataFrame(numpyArray)
print(df)

