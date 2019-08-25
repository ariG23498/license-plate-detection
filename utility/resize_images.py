import cv2
filename = 'car.jpg'
oriimg = cv2.imread(filename)
height, width, depth = oriimg.shape
newimg = cv2.resize(oriimg,(20,20))
cv2.imshow("Show by CV2",newimg)
cv2.waitKey(0)
cv2.imwrite("resizeimg.jpg",newimg)
