import tensorflow as tf

a = 1
b = 2
c = tf.add(a,b)
print(c)

with tf.Session() as sess:
    output = sess.run(c)
    print(output)
    sess.close()

