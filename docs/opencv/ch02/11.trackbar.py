import cv2
import numpy as np


def on_level_change(pos):
    value = pos * 16
    if value >= 255:
        value = 255

    img[:] = value
    cv2.imshow("image", img)


img = np.zeros((480, 640), np.uint8)

cv2.namedWindow("images")
cv2.createTrackbar("level", "images", 0, 100, on_level_change)

cv2.imshow("images", img)
cv2.waitKey()
cv2.destroyAllWindows()
