import cv2


img1 = cv2.imread("ch02/cat.bmp", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("ch02/cat.bmp", cv2.IMREAD_COLOR)

print("type(img1):", type(img1))
print("img1.shpe :", img1.shape)
print("img2.shpe :", img2.shape)
print("img2.dtype:", img2.dtype)

h, w = img2.shape[:2]
print("img2 size:{}x{}".format(w, h))

if len(img1.shape) == 2:
    print("img1 is a grayscale image")
else:
    print("img1 is a truecolor image")

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.waitKey()

cv2.destroyAllWindows()


img1 = cv2.imread("ch02/cat.bmp", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("ch02/cat.bmp", cv2.IMREAD_COLOR)

# for y in range(h):
#     for x in range(w):
#         img1[y, x] = 255
#         img2[y, x] = [0, 0, 255]

img1[50:350, 250:550] = 0
img2[50:350, 250:550] = (0, 0, 255)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.waitKey()

cv2.destroyAllWindows()
