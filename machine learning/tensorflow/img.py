import cv2
import numpy as np
import glob
from tqdm import tqdm
import imgaug as ia
from imgaug import augmenters as iaa
import tensorflow as tf


image_file="C://Users//junbo//Desktop//17290503195459.png"
path="C://Users//junbo//Desktop//weixin.jpg"
# img=cv2.imread(image_file)
# print(img.shape)

image_data = tf.gfile.FastGFile(image_file, 'rb').read()
if image_file[-4:]==".png":
    image_data = tf.image.decode_png(image_data,3)#3 represent output an RGB image
    print("png:",image_data)
else:
    image_data = tf.image.decode_jpeg(image_data)
# image_data = tf.expand_dims(image_data, 0)
with tf.Session() as sess:
    image_data = sess.run(image_data)
    print(image_data.shape)

cv2.imshow('image', image_data)
cv2.waitKey(0)











# ia.seed(1)
# count=1
# for img_2 in tqdm(glob.glob(r"C:\Users\junbo\Desktop\Identity\False\\*.jpg")):
#     # img_1=random.sample(glob.glob(r"C:\Users\junbo\Desktop\sfz\*.png"),1)[0]
#     #
#     # img1 = cv2.imread(img_1)
#     # img1 = cv2.resize(img1, (320, 200))
#     img2 = cv2.imread(img_2)
#     try:
#         img2 = cv2.resize(img2, (382, 382))
#     except:
#         print("error")
#         continue
#     # i = random.randint(2, 60)
#     # j = random.randint(2,180)
#     #
#     # img2[ j:200 + j, i:320 + i ] = img1
#     cv2.imwrite("C://Users//junbo//Desktop//Identity//error//{}.jpg".format(count),img2)
#     count+=1
#







