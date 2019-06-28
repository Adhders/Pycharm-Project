
import numpy as np
import cv2

bbox=np.array([413,380,917,496,895,592,391,477])
point_1=bbox[:2]
point_2=bbox[2:4]
point_3=bbox[4:6]
point_4=bbox[6:8]


img=cv2.imread(r"C:\Users\junbo\Desktop\test_2.png")
w0,w1=min(bbox[0],bbox[6]),max(bbox[2],bbox[4])
h0,h1=min(bbox[1],bbox[3]),max(bbox[5],bbox[7])

w=int(np.linalg.norm(point_1-point_2))
h=int(np.linalg.norm(point_2-point_3))

src=img[h0:h1,w0:w1]
cv2.imshow("src",src)

src_pts=np.float32([point_1,point_2,point_3])
dst_pts=np.float32([[0,0],[w,0],[w,h]])


src_pts1=np.array([point_1,point_2,point_3,point_4])
dst_pts1=np.array([[0,0],[w,0],[w,h],[0,h]])


img=cv2.imread(r"C:\Users\junbo\Desktop\test_2.png")
# circleIn = cv2.circle(img,center = tuple(point_2) , radius =1 , color = (0,255,0), thickness = 3)

x,y=point_2-point_1
print(x,y)
angle=np.arctan2(y,x)*(180/np.pi)
AffineMatrix=cv2.getAffineTransform(src_pts,dst_pts)

print(angle)
M = cv2.getRotationMatrix2D((int(h/2),int(w/2)),angle,1)
mat,_ = cv2.findHomography(src_pts1, dst_pts1) #求单应矩阵


im1Reg = cv2.warpAffine(src,M, (w,h))
im1Reg1 = cv2.warpAffine(img,AffineMatrix, (w,h))
im1Reg2=cv2.warpPerspective(img,mat,(w,h))
cv2.imshow("rotation",im1Reg)


cv2.waitKey(0)