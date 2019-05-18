# # coding=utf-8
import cv2
import numpy as np
#
# img = cv2.imread('C:\\Users\\junbo\\Desktop\\dog.png', 0)
# # OpenCV定义的结构元素
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
#
# # 腐蚀图像
# eroded = cv2.erode(img, kernel)
# # 显示腐蚀后的图像
# cv2.imshow("Eroded Image", eroded);
#
# # 膨胀图像
# dilated = cv2.dilate(img, kernel)
# # 显示膨胀后的图像
# cv2.imshow("Dilated Image", dilated);
# # 原图像
# cv2.imshow("Origin", img)
#
# # NumPy定义的结构元素
# NpKernel = np.uint8(np.ones((3, 3)))
# Nperoded = cv2.erode(img, NpKernel)
# # 显示腐蚀后的图像
# cv2.imshow("Eroded by NumPy kernel", Nperoded);
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

image=np.zeros((6,10))
image[3][2]=1
image[3][6]=1
image[3][7]=1
ker=np.ones((1,10),np.uint8)

print(image)
#kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5),(2,-1))
eroded = cv2.dilate(image, ker,(0,0))
print(eroded)