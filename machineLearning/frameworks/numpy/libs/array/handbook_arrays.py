import numpy as np

# # i. indexing
# # create a 2d array matrix and get value
# np.random.seed(0)
# x = np.random.randint(19, size=(3, 3))
# print(x)
# print("\n", x.shape)
# print(x[0, 2])
# # create a 3d matrix, and pull a row
# x = np.random.randint(19, size=(3, 3, 3))
# print(x)
# print("\n", x.shape)
# # print mtx, row, columns
# print(x[2, 1, 0:3])

# # ii. Slicing
# # 1-D subarrays, or vectors
# x = np.arange(9)
# print(x)
# # vals >= 5
# print(x[:5])
# # or after 5:
# print(x[5:])
# # or starting with a
# # and ending with b
# print(x[3:6])
#
# print("\n")

############################################

# # multidimensional subarrays
# # create a random 3x3 array from 1 - 9
# y = np.random.randint(9, size=(3,3))
# print(y)
# # print vals for row 2,
# # with a column stride of 2 (aka every other)
# print(y[:2, ::2])

################################################

# # iii. reshaping arrays
# grid = np.arange(9)
# print(grid)
# grid = grid.reshape((3, 3))
# print(grid)
# grid = grid.reshape((9, 1))
# print(grid)
# grid = grid.reshape((1, 9))
# print(grid)

#################################

# # iv. concatenation of arrays
# x = np.ndarray(shape=(3,3), dtype=int)
# y = np.ndarray(shape=(3,3), dtype=int)
# z = np.concatenate([x,y])
# q = np.concatenate([x, y, z])
# print(z)
# print(z.shape)
# print(q)
# print(q.shape)

#####################################



