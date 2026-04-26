import sys
import numpy as np
import cv2


src = cv2.imread("ch06/tekapo.bmp")

if src is None:
    print("Image load failed!")
    sys.exit()

# [x사용여부,x기울기,이동거리],[y축기울기 ,y축사용여부,이동거리]
aff = np.array([[1, 0.8, 0], [0.5, 1, 0]], dtype=np.float32)

dst = cv2.warpAffine(src, aff, (0, 0))

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()
