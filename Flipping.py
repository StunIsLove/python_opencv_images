import argparse
import imutils
import cv2

image = cv2.imread("image.png")
cv2.imshow("Original", image)

ﬂipped = cv2.ﬂip(image, 1)
cv2.imshow("Flipped Horizontally", ﬂipped)

ﬂipped = cv2.ﬂip(image, 0) 
cv2.imshow("Flipped Vertically", ﬂipped)

ﬂipped = cv2.ﬂip(image, -1) 
cv2.imshow("Flipped Horizontally & Vertically", ﬂipped) 

while True:
	#Ожидание ESC для закрытия (иначе окна появляются на секунду и исчезают)

	if cv2.waitKey(10) == 27:
		break