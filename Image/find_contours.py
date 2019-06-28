import cv2

img = cv2.imread(r'./img/contour.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
#findContours只接收BINARY图像
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#每个轮廓contours[i]对应4个hierarchy元素hierarchy[i][0] ~hierarchy[i][3]，
# 分别表示后一个轮廓、前一个轮廓、父轮廓、内嵌轮廓的索引编号，如果没有对应项，则该值为负数
print(hierarchy)

#分别显示轮廓
#cv2.drawContours(img, contours, 0, (0, 0, 255), 3)
#cv2.drawContours(img, contours, 1, (0, 0, 255), 3)

#显示所有轮廓
cv2.drawContours(img, contours, -1, (0, 0, 255), 3)
# 第三个参数指定绘制轮廓list中的哪条轮廓，如果是-1，则绘制其中的所有轮廓。后面的参数很简单。
# 其中thickness表明轮廓线的宽度，如果是-1（cv2.FILLED），则为填充模式

cv2.imshow("img", img)
cv2.waitKey(0)
