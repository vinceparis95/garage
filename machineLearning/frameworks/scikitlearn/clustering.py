import sklearn.cluster
import numpy as np
import matplotlib.pyplot as plt

array2 = np.ndarray(shape=(3, 3), dtype=int)
print(array2)

cluster = sklearn.cluster.k_means(array2, n_clusters=2)
print(cluster)