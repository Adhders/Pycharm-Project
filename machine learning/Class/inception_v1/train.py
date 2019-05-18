import os
import flowers
import tensorflow as tf
import tensorflow.contrib.slim as slim
from tensorflow.contrib.slim.nets import inception
import inception_preprocessing

image_size = inception.inception_v1.default_image_size
flowers_data_dir = './tfrecords'
checkpoints_dir = './checkpoints'
train_dir = './output'
_FILE_PATTERN = 'flowers_%s_*.tfrecord'

def load_batch(dataset, batch_size=32, height=299, width=299, is_training=False):
    """
    加载单个 bacth 的数据.

    Args:
      dataset: 待加载数据.
      batch_size: batch 内图片数量.
      height: 预处理后的每张图片的 height.
      width: 预处理后的每张图片的 width.
      is_training: 当前数据是否处于 training 还是 evaluating.

    Returns:
      images: [batch_size, height, width, 3] 大小的 Tensor, 预处理后的图片样本.
      images_raw: [batch_size, height, width, 3] 大小的 Tensor, 用于可视化的图片样本.
      labels: [batch_size] 大小的 Tensor, 其值范围为 [0，dataset.num_classes].
    """
    data_provider = slim.dataset_data_provider.DatasetDataProvider(
        dataset, common_queue_capacity=32, common_queue_min=8)
    image_raw, label = data_provider.get(['image', 'label.txt'])

    # Inception 的图片预处理.
    image = inception_preprocessing.preprocess_image(image_raw, height, width, is_training=is_training)

    # 预处理图片的可视化.
    image_raw = tf.expand_dims(image_raw, 0)
    image_raw = tf.image.resize_images(image_raw, [height, width])
    image_raw = tf.squeeze(image_raw)

    # Batch 化.
    images, images_raw, labels = tf.train.batch(
        [image, image_raw, label],batch_size=batch_size,
        num_threads=1, capacity=2 * batch_size)

    return images, images_raw, labels


def get_init_fn():
    """
    训练热身函数.
    权重参数初始化.
    """

    checkpoint_exclude_scopes=["InceptionV1/Logits", "InceptionV1/AuxLogits"]  #原输出层
    # finetune 时更改原输出层，初始化权重时，不更新输出层的权重参数
    exclusions = [scope.strip() for scope in checkpoint_exclude_scopes]

    variables_to_restore = []
    for var in slim.get_model_variables():
        for exclusion in exclusions:
            if var.op.name.startswith(exclusion):
                break
        else:
            variables_to_restore.append(var)

    return slim.assign_from_checkpoint_fn(
        os.path.join(checkpoints_dir, 'inception_v1.ckpt'),
        variables_to_restore)


if __name__=="__main__":
    with tf.Graph().as_default():
        tf.logging.set_verbosity(tf.logging.INFO)

        dataset = flowers.get_split('train', flowers_data_dir)
        images, _, labels = load_batch(dataset, height=image_size, width=image_size)

        # with tf.Session() as sess:
        #     coord = tf.train.Coordinator()
        #     threads = tf.train.start_queue_runners(sess, coord)
        #     print(sess.run((images,labels)))

        # 模型创建，采用默认的arg scope 配置 batch norm 参数.

        with slim.arg_scope(inception.inception_v1_arg_scope()):
            logits, _ = inception.inception_v1(images, num_classes=dataset.num_classes, is_training=True)

        # 设定 loss 函数:
        one_hot_labels = slim.one_hot_encoding(labels, dataset.num_classes)
        slim.losses.softmax_cross_entropy(logits, one_hot_labels)
        total_loss = slim.losses.get_total_loss()

        # 创建 summaries 以可视化训练过程:
        tf.summary.scalar('losses/Total Loss', total_loss)

        # 设定 optimizer，创建 train op:
        optimizer = tf.train.AdamOptimizer(learning_rate=0.01)
        train_op = slim.learning.create_train_op(total_loss, optimizer)

        # 开始训练:
        final_loss = slim.learning.train(train_op,
                                         logdir=train_dir,
                                         log_every_n_steps=10,
                                         init_fn=get_init_fn(),
                                         number_of_steps=3000,
                                         save_summaries_secs=600,
                                         save_interval_secs=1200)

    print('Finished training. Last batch loss %f' % final_loss)
