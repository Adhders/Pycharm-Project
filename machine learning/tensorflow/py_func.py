import tensorflow as tf
import numpy as np


def tile_b(tensor_a, tensor_b):
    tile_tensor_a = tf.py_func(_tile_b, [ tensor_a, tensor_b ], tf.float32)
    return tile_tensor_a


def _tile_b(a, b):
    if a[0]==1.:
        tile_b = np.tile(b, (4, 1))
    else:
        tile_b = b
    return tile_b


def main():
    a = tf.placeholder(tf.float32, shape=[1], name = "tensor_a")
    b = tf.placeholder(tf.float32, shape=[1, 2], name = "tensor_b")
    tile_tensor_b = tile_b(a, b)
    sess = tf.Session()
    array_a = np.array([1.])
    array_b = np.array([[2., 3.]])
    feed_dict = {a: array_a, b: array_b}
    tile_b_value = sess.run(tile_tensor_b, feed_dict = feed_dict)
    print(tile_b_value)

if __name__ == '__main__':
    main()