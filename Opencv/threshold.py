import cv2
import matplotlib.pyplot as plt

img = cv2.imread('C:\\Users\\junbo\\Desktop\\star.jpg',0) #直接读为灰度图像
# ret1,thresh1 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# ret2,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
# ret3,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
# ret4,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
# ret5,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
# titles = ['img','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
# images = [img,thresh1,thresh2,thresh3,thresh4,thresh5]
# print(ret1,ret2,ret3,ret4,ret4,ret5)
# for i in range(6):
#     plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()

ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
cv2.THRESH_BINARY,11,2) #换行符号 \
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
cv2.THRESH_BINARY,11,2) #换行符号 \
images = [img,th1,th2,th3]
plt.figure()
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
plt.show()