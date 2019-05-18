from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import math
import os
import random
import sys

import tensorflow as tf

import dataset_utils

# 验证数据集的图片数.
_NUM_VALIDATION = 300

# Seed for repeatability.
_RANDOM_SEED = 0

# The number of shards per dataset split.
_NUM_SHARDS = 5


class ImageReader(object):
  """
  用于 TensorFlow 图片编码的辅助类
  """

  def __init__(self):
    # 初始化解码decode RGB JPEG 格式数据的函数.
    self._decode_jpeg_data = tf.placeholder(dtype=tf.string)
    self._decode_jpeg = tf.image.decode_jpeg(self._decode_jpeg_data, channels=3)

  def read_image_dims(self, sess, image_data):
    image = self.decode_jpeg(sess, image_data)
    return image.shape[0], image.shape[1]

  def decode_jpeg(self, sess, image_data):
    image = sess.run(self._decode_jpeg,
                     feed_dict={self._decode_jpeg_data: image_data})
    assert len(image.shape) == 3
    assert image.shape[2] == 3
    return image


def _get_filenames_and_classes(dataset_dir):
  """
  返回文件名和类别名列表.

  Args:
    dataset_dir: 包含多个图片子路径的路径.
    class names. 每个图片子路径包含 PNG 或 JPG 编码的图片.
  Returns:
    图片文件列表，相对于 `dataset_dir`；
    图片子路经列表，表示类比名字.
  """
  flower_root = os.path.join(dataset_dir, '')
  directories = []
  class_names = []
  for filename in os.listdir(flower_root):
    path = os.path.join(flower_root, filename)
    if os.path.isdir(path):
      directories.append(path)
      class_names.append(filename)

  photo_filenames = []
  for directory in directories:
    for filename in os.listdir(directory):
      path = os.path.join(directory, filename)
      photo_filenames.append(path)

  return photo_filenames, sorted(class_names)


def _get_dataset_filename(dataset_dir, split_name, shard_id):
  output_filename = 'flowers_%s_%05d-of-%05d.tfrecord' % (
      split_name, shard_id, _NUM_SHARDS)
  return os.path.join(dataset_dir, output_filename)


def _convert_dataset(split_name, filenames, class_names_to_ids, dataset_dir):
  """
  将给定文件名转换为 TFRecord 格式数据集.

  Args:
    split_name: 数据集的名字，train 或 validation.
    filenames: png 或 jpg 图片的绝对路径列表.
    class_names_to_ids: 类别名字(字符串strings) 到类别 ids(整数integers ) 映射的字典.
    dataset_dir: 转换后的 TFRecord 数据集所保存的路径.
  """
  assert split_name in ['train', 'validation']

  num_per_shard = int(math.ceil(len(filenames) / float(_NUM_SHARDS)))

  with tf.Graph().as_default():
    image_reader = ImageReader()

    with tf.Session('') as sess:

      for shard_id in range(_NUM_SHARDS):
        output_filename = _get_dataset_filename(dataset_dir, split_name, shard_id)

        with tf.python_io.TFRecordWriter(output_filename) as tfrecord_writer:
          start_ndx = shard_id * num_per_shard
          end_ndx = min((shard_id+1) * num_per_shard, len(filenames))
          for i in range(start_ndx, end_ndx):
            sys.stdout.write('\r>> Converting image %d/%d shard %d' % (
                i+1, len(filenames), shard_id))
            sys.stdout.flush()

            # 读取文件名数据:
            image_data = tf.gfile.FastGFile(filenames[i], 'rb').read()
            height, width = image_reader.read_image_dims(sess, image_data)

            class_name = os.path.basename(os.path.dirname(filenames[i]))
            class_id = class_names_to_ids[class_name]

            example = dataset_utils.image_to_tfexample(
                image_data, b'jpg', height, width, class_id)
            tfrecord_writer.write(example.SerializeToString())

  sys.stdout.write('\n')
  sys.stdout.flush()





def _dataset_exists(dataset_dir):
  for split_name in ['train', 'validation']:
    for shard_id in range(_NUM_SHARDS):
      output_filename = _get_dataset_filename(
          dataset_dir, split_name, shard_id)
      if not tf.gfile.Exists(output_filename):
        return False
  return True


def run(dataset_dir,save_dir):
  """
  运行数据集下载和转换.

  Args:
    dataset_dir: 数据集所在的路径.
  """
  if not tf.gfile.Exists(dataset_dir):
    tf.gfile.MakeDirs(dataset_dir)

  if _dataset_exists(save_dir):
    print('Dataset files already exist. Exiting without re-creating them.')
    return

  # 如果已经下载解压过 Flowers 数据集，可以跳过此步.
  # dataset_utils.download_and_uncompress_tarball(_DATA_URL, dataset_dir)

  photo_filenames, class_names = _get_filenames_and_classes(dataset_dir)
  class_names_to_ids = dict(zip(class_names, range(len(class_names))))

  # 数据集分为：train 和 test:
  random.seed(_RANDOM_SEED)
  random.shuffle(photo_filenames)
  training_filenames = photo_filenames[_NUM_VALIDATION:]
  validation_filenames = photo_filenames[:_NUM_VALIDATION]

  # 首先, 分别转换 training 和 validation 数据集.
  _convert_dataset('train', training_filenames, class_names_to_ids, save_dir)
  _convert_dataset('validation', validation_filenames, class_names_to_ids, save_dir)

  # 最后, 写入标签label 文件:
  labels_to_class_names = dict(zip(range(len(class_names)), class_names))
  dataset_utils.write_label_file(labels_to_class_names, save_dir)

  print('\nFinished converting the flowers dataset!')


if __name__ == '__main__':
    dataset_dir = r'F:/Data/flower_photos'
    save_dir="./tfrecords"
    run(dataset_dir,save_dir)
    print('Done.')