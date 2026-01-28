import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt


def img_add():
    img1 = cv2.imread("ch01/cv_test_img/cry.jpg")
    img2 = cv2.imread("ch03/tekapo.bmp")

    img1 = cv2.resize(img1, (img2.shape[1], img2.shape[0]))

    # result_img = cv2.add(img1, img2)
    result_img = cv2.addWeighted(img1, 0.8, img2, 0.2, -1)

    cv2.imshow("Result Image", result_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


src1 = cv2.imread("ch03/lenna256.bmp", cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread("ch03/square.bmp", cv2.IMREAD_GRAYSCALE)

if src1 is None or src2 is None:
    print("image load failed")
    sys.exit()

dst1 = cv2.add(src1, src2, dtype=cv2.CV_8U)
dst2 = cv2.addWeighted(src1, 0.5, src2, 0.5, 0.0)
dst3 = cv2.subtract(src1, src2)
dst4 = cv2.absdiff(src1, src2)

plt.subplot(231), plt.axis("off"), plt.imshow(src1, "gray"), plt.title("src1")
plt.subplot(232), plt.axis("off"), plt.imshow(src2, "gray"), plt.title("src2")
plt.subplot(233), plt.axis("off"), plt.imshow(dst1, "gray"), plt.title("dst1")
plt.subplot(234), plt.axis("off"), plt.imshow(dst2, "gray"), plt.title("dst2")
plt.subplot(235), plt.axis("off"), plt.imshow(dst3, "gray"), plt.title("dst3")
plt.subplot(236), plt.axis("off"), plt.imshow(dst4, "gray"), plt.title("dst4")
plt.show()
