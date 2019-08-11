# this classifier can be used with a bunch of different models
# here, you see a ResNet50 keras model that can classify animals,
# like a honey badger :)

from tensorflow.python.keras.applications.resnet50 import ResNet50
from tensorflow.python.keras.preprocessing import image
from tensorflow.python.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np

model = ResNet50()

img_path = '/home/vince/Desktop/honeybadger.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

preds = model.predict(x)
print(decode_predictions(preds, top=4))