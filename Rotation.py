import numpy as np 
import argparse 
import imutils 
import cv2

image = cv2.imread("image.png") 
cv2.imshow("Original", image)

(h, w) = image.shape[:2]
(cX, cY) = (w / 2, h / 2)

M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
rotated = cv2.warpAfﬁne(image, M, (w, h))
cv2.imshow("Rotated by 45 Degrees", rotated)

M = cv2.getRotationMatrix2D((cX, cY), -90, 1.0)
rotated = cv2.warpAfﬁne(image, M, (w, h))
cv2.imshow("Rotated by -90 Degrees", rotated)

while True:
	#Ожидание ESC для закрытия (иначе окна появляются на секунду и исчезают)

	if cv2.waitKey(10) == 27:
		break