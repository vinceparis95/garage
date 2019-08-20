import numpy as np
import pandas as pd
import tensorflow as tf
import keras
from tensorflow import feature_column
from tensorflow.python.keras import layers
from sklearn.model_selection import train_test_split

csv = "/home/vince/Desktop/youthy.csv"
df = pd.read_csv(csv)
print(df.head())

train, test = train_test_split(df, test_size=0.2)
train, val = train_test_split(train, test_size=0.2)
print(len(train), 'train examples')
print(len(val), 'validation examples')
print(len(test), 'test examples')


# A utility method to create a tf.data dataset from a Pandas Dataframe
def df_to_dataset(dataframe, shuffle=True, batch_size=32):
  dataframe = dataframe.copy()
  labels = dataframe.pop('Trained')

  ds = tf.data.Dataset.from_tensor_slices((dict(dataframe), labels))
  if shuffle:
    ds = ds.shuffle(buffer_size=len(dataframe))
  ds = ds.batch(batch_size)
  return ds

batch_size = 5
# A small batch sized is used for demonstration purposes
train_ds = df_to_dataset(train, batch_size=batch_size)
val_ds = df_to_dataset(val, shuffle=False, batch_size=batch_size)
test_ds = df_to_dataset(test, shuffle=False, batch_size=batch_size)
for feature_batch, label_batch in train_ds.take(1):
  print('Every feature:', list(feature_batch.keys()))
  print('A batch of neighborhoods:', feature_batch['Neighborhood'])
  print('A batch of ages:', label_batch )


# We will use this batch to demonstrate several types of feature columns
example_batch = next(iter(train_ds))[0]


# A utility method to create a feature column
# and to transform a batch of data
def demo(feature_column):
  feature_layer = tf.compat.v1.keras.layers.DenseFeatures(feature_column)
  print(feature_layer(example_batch).numpy())


# based on TensorFlow mL basics classifier for structured data
