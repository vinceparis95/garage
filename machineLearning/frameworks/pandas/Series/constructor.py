import pandas as pd
import numpy as np
import tensorflow as tf

# # i. create a pandas Series
# series = pd.Series([[1, 2, 3], [3, 2, 1], [5, 5, 5]])
# print(series)
# print(series.values)
# print(series.shape)

##########################################

# # ii. create a series from a numpy array
# array = np.array([1, 5, 9])
# series = pd.Series(array)
# # print the nth item
# print(series[1])

#########################################

# # iii. create a series from a column of csv data
# csv = pd.read_csv("/home/vince/Desktop/youthy.csv")
# csv_series = pd.Series(csv['Age'])
# csv_series_b = pd.Series(csv['Neighborhood'])
# # print(csv_series)
# # print(csv_series_b)
# print(csv_series_b.head(5))

#############################################

# # iv. create a series from a python dictionary
# population_dict = {'California': 38332521,
#                    'Texas': 26448193,
#                    'New York': 19651127,
#                    'Florida': 19552860,
#                    'Illinois': 12882135}
# population = pd.Series(population_dict)
# print(population)

##############################################