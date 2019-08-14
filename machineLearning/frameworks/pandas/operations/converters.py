import pandas as pd
import numpy as np

# CSV elements

# # > Load csv to pandas
# df = pd.read_csv('/home/vince/Desktop/pima.csv')
# print(df)

# > create DataFrame from numpy array
array = np.ones(shape=(3, 3))
df = pd.DataFrame(data=array)
print(df)


