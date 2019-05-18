
import tensorflow as tf
import numpy as np
from tensorflow.models.tutorials.rnn.ptb import reader
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

DATA_PATH='D:\Project\Python project\Machine Learning\PTB\data'
train_data,valid_data,test_data,_=reader.ptb_raw_data(DATA_PATH)

def ptb_producer(raw_data, batch_size, num_steps, name=None):



    with tf.name_scope(name, "PTBProducer", [raw_data, batch_size, num_steps]):

        raw_data = tf.convert_to_tensor(raw_data, name="raw_data", dtype=tf.int32)

        data_len = tf.size(raw_data)
        batch_len = data_len // batch_size
        data = tf.reshape(raw_data[0 : batch_size * batch_len],
                      [batch_size, batch_len])

        epoch_size = (batch_len - 1) // num_steps

    for i in range(epoch_size.eval()):
        x=[],y=[]
        tmp_x= tf.strided_slice(data, [0, i * num_steps],
                         [batch_size, (i + 1) * num_steps])
        tmp_x.set_shape([batch_size, num_steps])
        x=x.append(tmp_x)
        tmp_y = tf.strided_slice(data, [0, i * num_steps + 1],
                         [batch_size, (i + 1) * num_steps + 1])
        tmp_y.set_shape([batch_size, num_steps])
        y=yappend(tmp_y)
    return x, y
with tf.Session() as sess:
    tf.global_variables_initializer().run()
    x,y=ptb_producer(train_data,4,5)
    print(sess.run(tf.shape(x)))
    print(sess.run(tf.shape(y)))

