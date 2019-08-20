import pandas as pd

# df.pop gives us just the row we wanted
dataframe = pd.read_csv("/home/vince/Desktop/youthy.csv")
labels = dataframe.pop('Age')
print(labels)