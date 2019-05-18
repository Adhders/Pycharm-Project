import numpy as np
import tensorflow as tf
slim = tf.contrib.slim

def next_batch():
    datasets = np.asarray(range(0, 24))
    input_queue = tf.train.slice_input_producer([ datasets ], shuffle=False, num_epochs=1)
    data_batchs = tf.train.batch(input_queue, batch_size=5, num_threads=1,
                                 capacity=20, allow_smaller_final_batch=False)

    #prefetch_queue.prefetch_queue可以节约数据打包时间
    data_batchs = slim.prefetch_queue.prefetch_queue(
        [data_batchs],capacity=50)
    return data_batchs


if __name__ == "__main__":
    data_batchs = next_batch()
    sess = tf.Session()
    sess.run(tf.local_variables_initializer())
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess, coord)
    try:
        while not coord.should_stop():
            # print(sess.run([ data_batchs ])) #

            data = data_batchs.dequeue()

            print(sess.run(data))

    except tf.errors.OutOfRangeError:
        print("complete")
    finally:
        coord.request_stop()
    coord.join(threads)
    sess.close()
