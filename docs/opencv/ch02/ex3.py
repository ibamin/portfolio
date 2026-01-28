import cv2

img1 = cv2.imread("ch02/HappyFish.jpg")

img2 = img1
img3 = img1.copy()

img1.fill(255)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("img3", img3)
cv2.waitKey()
cv2.destroyAllWindows()


img1 = cv2.imread("ch02/HappyFish.jpg")
img2 = img1[40:120, 30:150]
img3 = img1[40:120, 30:150].copy()

img2.fill(0)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("img3", img3)
cv2.waitKey()
cv2.destroyAllWindows()
