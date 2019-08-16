import tensorflow as tf

w = tf.Variable(([3, 3, 3], [1, 3, 5], [9, 19, 95]), name='3x3')
print(w)

# with tf.compat.v1.Session() as sess:
#     sess.run(w.initializer)
#     sess.close()
