import tensorflow as tf
from tensorflow import keras
import pandas as pd

# mL/frameworks/pandas/operations/csv_converters
# prepare the data
# # Load csv to pandas
df = pd.read_csv('/home/vince/Desktop/youthy.csv')
print(df)

# # replace matrix values with 1 or 0
df2 = df.replace(to_replace=[19, 'cobbs', 'no'], value=0)
df3 = df2.replace(to_replace=[17, 18, 'cedar', 'yes'], value=1)
print(df3)

# # create two matrices,
# # one for input, and one for output
dfInput = df3[['Age', 'Neighborhood', 'Attended']]
dfInput = dfInput.as_matrix()
print(dfInput)
dfOutput = df3[['Trained']]
dfOutput = dfOutput.as_matrix()
print(dfOutput)

# # create tensors from matrices
# # print shape to verify
inputTensor = tf.Variable(dfInput, dtype=float)
print(inputTensor.shape)
outputTensor = tf.Variable(dfOutput, dtype=float)
print(outputTensor.shape)
print(inputTensor)
print(outputTensor)
# # tensors should now be prepared to flow through network

##########################################################

# build the neural network
# # define a sequential model
model = keras.Sequential()

# # define an input and an output layer,
# # and add them each to the model
input_layer = keras.layers.Dense(3, input_shape=[3], activation='tanh')
model.add(input_layer)
output_layer = keras.layers.Dense(1, activation='sigmoid')
model.add(output_layer)

# # add the optimizer
gradientDescender = tf.optimizers.Adam(0.01)

# # compile and fit the network
model.compile(optimizer=gradientDescender,
              loss='mean_squared_error')
model.fit(inputTensor, outputTensor, epochs=1000, steps_per_epoch=10)

# # test the network
results = model.predict(inputTensor, verbose=1, steps=1)
print(results)

