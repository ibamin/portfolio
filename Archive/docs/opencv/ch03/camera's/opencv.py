import cv2


def main():
    camera = cv2.VideoCapture(0)
    camera.set(3, 320)
    camera.set(4, 240)

    while 1:
        _, frame = camera.read()
        cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) == ord("q"):
            break

    camera.release()
    cv2.destoryAllWindows()


if __name__ == "__main__":
    main()
