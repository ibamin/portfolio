import sys
import numpy as np
import cv2


def on_color_change(pos):
    value = pos * 16
    if value >= 255:
        value = 255
    modified_image = cv2.add(src, value)
    cv2.imshow("lenna", modified_image)


# 그레이스케일 영상 불러오기
src = cv2.imread("ch03/lenna.bmp", cv2.IMREAD_GRAYSCALE)

if src is None:
    print("Image load failed!")
    sys.exit()

cv2.namedWindow("lenna")
cv2.createTrackbar("color", "lenna", 0, 15, on_color_change)

cv2.imshow("lenna", src)
cv2.waitKey(0)
cv2.destroyAllWindows()
