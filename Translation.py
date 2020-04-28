import numpy as np
import argparse
import imutils
import cv2

image = cv2.imread("image.png")
cv2.imshow("Original", image)

M = np.ﬂoat32([[1, 0, 25], [0, 1, 50]])
shifted = cv2.warpAfﬁne(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Down and Right", shifted)

M = np.ﬂoat32([[1, 0, -50], [0, 1, -90]])
shifted = cv2.warpAfﬁne(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Up and Left", shifted)

while True:
	#Ожидание ESC для закрытия (иначе окна появляются на секунду и исчезают)

	if cv2.waitKey(10) == 27:
		break