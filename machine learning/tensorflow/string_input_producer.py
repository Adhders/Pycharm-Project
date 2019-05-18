import tensorflow as tf

# 新建一个Session
with tf.Session() as sess:
    # 我们要读三幅图片A.jpg, B.jpg, C.jpg
    filename = ['2.jpg', '1.jpg']
    # string_input_producer会产生一个文件名队列
    filename_queue = tf.train.string_input_producer(filename, shuffle=True, num_epochs=5)
    # reader从文件名队列中读数据。对应的方法是reader.read
    reader = tf.WholeFileReader()
    key, value = reader.read(filename_queue)#key表示文件名
    tf.local_variables_initializer().run()
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)
    i = 0
    try:
        # while not coord.should_stop():
        while True:
            i += 1
            print(sess.run(key))
            # image_data = sess.run(value)
            # with open('read/test_%d.jpg' % i, 'wb') as f:
            #     f.write(image_data)
    except :
        # When done, ask the threads to stop.
        print('Done training -- epoch limit reached')
    finally:
        coord.request_stop()
        # Wait for threads to finish.
    coord.join(threads)