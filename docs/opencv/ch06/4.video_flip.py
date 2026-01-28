import cv2

img = cv2.imread("ch06/tekapo.bmp")

dst1 = cv2.flip(img, 1)
dst2 = cv2.flip(img, 0)
dst3 = cv2.flip(img, -1)

cv2.imshow("Origin", img)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.imshow("dst3", dst3)

cv2.waitKey()
cv2.destroyAllWindows()
