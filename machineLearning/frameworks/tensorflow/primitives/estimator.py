import tensorflow as tf
print(tf.version)

a = tf.constant(5)
b = tf.constant(9)
res = tf.add(a, b)
print(res)
