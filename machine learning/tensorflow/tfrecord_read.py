import tensorflow as tf


reader = tf.TFRecordReader()
filename_queue = tf.train.string_input_producer([r"C:\Users\junbo\Desktop\python2.tfrecord"])

_,serialized_example = reader.read(filename_queue)

features = tf.parse_single_example(
    serialized_example,
    features={
        'image/encoded': tf.FixedLenFeature((), tf.string, default_value=''),
        'image/format': tf.FixedLenFeature((), tf.string, default_value='jpeg'),
        'image/filename': tf.FixedLenFeature((), tf.string, default_value=''),
        'image/shape': tf.FixedLenFeature([ 3 ], tf.int64),
        'image/object/bbox/xmin': tf.VarLenFeature(dtype=tf.float32),
        'image/object/bbox/ymin': tf.VarLenFeature(dtype=tf.float32),
        'image/object/bbox/xmax': tf.VarLenFeature(dtype=tf.float32),
        'image/object/bbox/ymax': tf.VarLenFeature(dtype=tf.float32),
        'image/object/bbox/x1': tf.VarLenFeature(dtype=tf.float32),
        'image/object/bbox/x2': tf.VarLenFeature(dtype=tf.float32),
        'image/object/bbox/x3': tf.VarLenFeature(dtype=tf.float32),
        'image/object/bbox/x4': tf.VarLenFeature(dtype=tf.float32),
        'image/object/bbox/y1': tf.VarLenFeature(dtype=tf.float32),
        'image/object/bbox/y2': tf.VarLenFeature(dtype=tf.float32),
        'image/object/bbox/y3': tf.VarLenFeature(dtype=tf.float32),
        'image/object/bbox/y4': tf.VarLenFeature(dtype=tf.float32),
        'image/object/bbox/label': tf.VarLenFeature(dtype=tf.int64),
    })

# images = tf.decode_raw(features['image_raw'],tf.uint8)
filename=tf.cast(features["image/filename"],tf.string)
xmin = tf.cast(features['image/object/bbox/xmin'],tf.float32)
ymin = tf.cast(features['image/object/bbox/ymin'],tf.float32)
x1=tf.cast(features['image/object/bbox/x1'],tf.float32)
shape=tf.cast(features['image/shape'],tf.int64)
label=tf.cast(features['image/object/bbox/label'],tf.int64)

with tf.Session() as sess:

    # 启动多线程处理输入数据。
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess,coord=coord)

    for i in range(1):
        print(sess.run([x1]))