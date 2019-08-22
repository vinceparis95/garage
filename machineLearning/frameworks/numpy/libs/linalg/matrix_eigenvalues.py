import numpy as np
from numpy import linalg as LA

A = np.array([[1, 5, 9], [19, 95, 361],[1, 1, 1]])
w, v = LA.eig(A)
print(w)
print(v)