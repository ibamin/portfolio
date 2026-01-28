import matplotlib.pyplot as plt
import cv2


def default():
    imgBGR = cv2.imread("ch01/cat.bmp")
    imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)

    plt.axis("on")  # x,y축 그리기 옵션 설정
    plt.imshow(imgRGB)
    plt.show()

    imgGray = cv2.imread("ch01/cat.bmp", cv2.IMREAD_GRAYSCALE)

    plt.axis("off")
    plt.imshow(imgGray, cmap="gray")
    plt.show()


def sub_print():
    imgBGR = cv2.imread("ch01/cat.bmp")
    imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
    imgGray = cv2.imread("ch01/cat.bmp", cv2.IMREAD_GRAYSCALE)

    plt.subplot(121), plt.axis("off"), plt.imshow(imgRGB)
    plt.subplot(122), plt.axis("off"), plt.imshow(imgGray)
    plt.show()


def multi_print(img_paths):
    num_images = len(img_paths)
    rows = (num_images + 2) // 3

    plt.figure(figsize=(12, 8))  # 그림 사이즈 지정

    for i, img_path in enumerate(img_paths, start=1):
        imgBGR = cv2.imread(img_path)
        imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)

        plt.subplot(rows, min(3, num_images), i)
        plt.imshow(imgRGB)
        plt.axis("off")

    plt.tight_layout()
    plt.show()


img_paths = [
    "ch01/cv_test_img/angly.jpg",
    "ch01/cv_test_img/cry.jpg",
    "ch01/cv_test_img/default.jpg",
    "ch01/cv_test_img/guess.jpg",
    "ch01/cv_test_img/sad.jpg",
]

multi_print(img_paths)
