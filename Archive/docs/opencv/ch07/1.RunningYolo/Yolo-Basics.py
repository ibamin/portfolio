from ultralytics import YOLO
import cv2

src = cv2.imread("ch07/1.RunningYolo/Images/OIP.jpg")
src = cv2.resize(src, (1280, 720), cv2.INTER_AREA)

model = YOLO("ch07/Yolo-Weights/yolov8n.pt")
results = model(src, show=True)
cv2.waitKey(0)
