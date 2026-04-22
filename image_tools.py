import cv2
import numpy as np

image = cv2.imread("sandeep.jpeg")
kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
frame = cv2.filter2D(image,-1, kernel)

blur = cv2.GaussianBlur(image,(5,5),0)
blured = cv2.medianBlur(image,5)
if image is not None:
    cv2.imshow("blur", blur)
    cv2.imshow("blured", blured)
    cv2.imshow("frame", frame)
    cv2.imshow("image", image)
# cv2.imshow("image2", image2)
    cv2.waitKey(0)