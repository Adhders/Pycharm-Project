import tensorflow as tf
from tensorflow.python.platform import tf_logging as logging

a=tf.constant(1)
b=tf.constant(2)
# logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
#                     level=logging.DEBUG)
with tf.Session() as sess:
    logging.set_verbosity(logging.DEBUG)
    logging.info("the result")

    print(sess.run(a+b))