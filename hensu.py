import tensorflow as tf

x = tf.constant(1, name='x')
y = tf.Variable(x + 2, name='y')

model = tf.initialize_local_variables()
with tf.Session() as session:
    session.run(model)
    print(session.run(y))
