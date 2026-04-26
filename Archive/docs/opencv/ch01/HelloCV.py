import cv2
import sys

print("hello opencv", cv2.__version__)


def img_print(img_path):
    img = cv2.imread(img_path)

    if img is None:
        print("Cat.bmp file is null")
        sys.exit()

    cv2.namedWindow("pepe", cv2.WINDOW_NORMAL)
    cv2.imshow("pepe", img)
    cv2.resizeWindow("pepe", 300, 300)
    cv2.waitKeyEx(0x270000)

    cv2.destroyAllWindows()


img_paths = [
    "ch01/cv_test_img/angly.jpg",
    "ch01/cv_test_img/cry.jpg",
    "ch01/cv_test_img/default.jpg",
    "ch01/cv_test_img/guess.jpg",
    "ch01/cv_test_img/sad.jpg",
]

for img in img_paths:
    img_print(img)
