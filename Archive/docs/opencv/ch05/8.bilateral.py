import sys
import numpy as np
import cv2

src = cv2.imread("ch05/lenna.bmp")

if src is None:
    print("Image load failed!")
    sys.exit()

# 3번째 매개변수는 엣지와 가우시안필터 적용할 기준
dst = cv2.bilateralFilter(src, -1, 10, 5)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()

cv2.destroyAllWindows()
