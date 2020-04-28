import argparse
import imutils
import cv2

image = cv2.imread("image.png")
cv2.imshow("Original", image)

crop = image[85:250, 85:220] 
cv2.imshow("Croped", crop) 

while True:
	#Ожидание ESC для закрытия (иначе окна появляются на секунду и исчезают)

	if cv2.waitKey(10) == 27:
		break