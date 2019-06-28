#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Copyright by 
# Author: Junbo
# Time : 2019/6/27 16:59

import cv2
import numpy as np


img=cv2.imread(r"./img/segmap.jpg")
#cv::IMREAD_GRAYSCALE = 0
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours_1 = np.roll(np.array(np.where(binary!= 0)), 1, axis=0).transpose().reshape(-1, 2)
# np.where()如果只含有条件且矩阵的shape为(n,m),则返回结果为n个(1,k)维度的numpy.ndarray,k代表满足条件的个数

contours_2, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours_2, -1, (0, 0, 255), 3)

rectangle_2 = cv2.minAreaRect(contours_2[0])  # minAreaRect函数参数是图像坐标点集
rectangle_1 = cv2.minAreaRect(contours_1)

box_2 = cv2.boxPoints(rectangle_2)
box = cv2.boxPoints(rectangle_1)
# make clock-wise order
startidx = box.sum(axis=1).argmin()  # 因为框倾斜角较小，坐标之和最小的是左上角
box = np.roll(box, 4 - startidx, 0)
print(box)



