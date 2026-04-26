import cv2
import time


def main():
    camera = cv2.VideoCapture(0)
    camera.set(3, 640)
    camera.set(4, 480)

    xml = (
        "C:/MyMoble/OpenCV/opencv/data/haarcascades/haarcascade_frontalface_default.xml"
    )
    face_cascade = cv2.CascadeClassifier(xml)

    while camera.isOpened():
        _, image = camera.read()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.05, 5)
        print("faces detected Number: " + str(len(faces)))

        if len(faces):
            for x, y, w, h in faces:
                face_roi = image[y : y + h, x : x + w]
                # 가우시안 블러 적용
                blurred_face = cv2.GaussianBlur(face_roi, (25, 25), 0)
                # 원본 이미지에 블러 처리된 얼굴 영역 복사
                image[y : y + h, x : x + w] = blurred_face
                cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imshow("Result", image)
        time.sleep(0.2)
        if cv2.waitKey(1) == ord("q"):
            break
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
