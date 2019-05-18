import numpy as np
import imutils
import cv2

image = cv2.imread("rotate.jpg")

a=np.array([56,306,0,130,438,0,492,174])
vector_1=a[0:2]
vector_2=a[2:4]
vector_4=a[6:8]
l1=np.linalg.norm(vector_2-vector_1)
l2=np.linalg.norm(vector_4-vector_1)
y=(vector_4-vector_1)[1]
x=(vector_4-vector_1)[0]
angle=-np.arctan2(y,x)*180/np.pi

w=int(l2)
h=int(l1)
print(w,h)
print(angle)


rotated = imutils.rotate_bound(image, angle)
shape = rotated.shape[ :2 ]
center = (int(shape[ 1 ] / 2), int(shape[ 0 ] / 2))
cv2.circle(rotated,center,2, (0, 0, 255), -1)
x1=int(center[0]-w/2)
y1=int(center[1]-h/2)
cv2.circle(rotated,(x1,y1),2, (0, 0, 255), -1)#左上角
cv2.circle(rotated,(x1+w,y1+h),2, (0, 0, 255), -1)#右下角
print(x1,y1)
print(rotated.shape)
crop_image=rotated[y1:y1+h,x1:x1+w:]
print(crop_image.shape)
cv2.imshow("Rotated (Correct)",crop_image)
cv2.waitKey(0)

