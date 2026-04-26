from ultralytics import YOLO
import cv2
import cvzone
import math
import time

cap = cv2.VideoCapture(cv2.CAP_DSHOW + 0)
cap.set(3, 640)
cap.set(4, 480)

model = YOLO("C:/MyMoble/OpenCV/ch07/Yolo-Weights/yolov8l.pt")

while 1:
    success, img = cap.read()
    results = model(img, stream=True)

    for r in results:
        boxes = r.boxes

        print(len(boxes))
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            print("tensor x1,y1,x2,y2", x1, y1, x2, y2)
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            print("x1, y1, x2, y2 ", x1, y1, x2, y2)
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
