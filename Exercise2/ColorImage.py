import numpy as np
import cv2
#g:\\601\\OpencvHomework\\
image = cv2.imread("Lenna.png")
cv2.imshow("Original",image)
#cv2.waitKey(0)

#BGR
(B,G,R) = cv2.split(image)
cv2.imshow("Red",R)
cv2.imshow("Green",G)
cv2.imshow("Blue",B)


imgYCC = cv2.cvtColor(image, cv2.COLOR_RGB2YCrCb)
(Y,Cb,Cr) = cv2.split(imgYCC)
cv2.imshow("Y",Y)
cv2.imshow("Cb",Cb)
cv2.imshow("Cr",Cr)

imgHSV = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
(H,S,V) = cv2.split(imgHSV)
cv2.imshow("Hue",H)
cv2.imshow("Saturation",S)
cv2.imshow("Value",V)
(b,g,r) = image[20,25]
(y,cb,cr) = imgYCC[20,25]
(h,s,v) = imgHSV[20,25]
print(r,g,b)
print(y,cb,cr)
print(h,s,v)
cv2.waitKey(0)