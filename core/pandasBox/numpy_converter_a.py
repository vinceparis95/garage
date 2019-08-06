import numpy as np
import pandas as pd

numpyArray = np.array([[1, 2, 3], [3, 2, 1]])
print(numpyArray.shape)

df = pd.DataFrame(numpyArray)

print(df)
