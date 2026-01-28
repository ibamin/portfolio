import sys
import numpy as np
import cv2


src = cv2.imread("ch06/namecard_moble.jpeg")

if src is None:
    print("Image load failed!")
    sys.exit()

w, h = 720, 400
srcQuad = np.array([[186, 760], [689, 474], [873, 733], [321, 1058]], np.float32)
dstQuad = np.array([[0, 0], [w - 1, 0], [w - 1, h - 1], [0, h - 1]], np.float32)

pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
dst = cv2.warpPerspective(src, pers, (w, h))

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()
