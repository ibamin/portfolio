import sys
import cv2


# 비디오 파일 열기
cap = cv2.VideoCapture(
    "ch02\myvideo.mp4.mp4\신의 한수! 생애 첫우승이 걸린 순간! [ASL 시즌14 결승전 6경기 김지성vs유영진].mp4"
)

fps = round(cap.get(cv2.CAP_PROP_FPS))
delay = round(1000 / fps)

if not cap.isOpened():
    print("Video open failed!")
    sys.exit()

# 비디오 프레임 크기, 전체 프레임수, FPS 등 출력
print("Frame width:", int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print("Frame height:", int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print("Frame count:", int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))

fps = cap.get(cv2.CAP_PROP_FPS)
print("FPS:", fps)

delay = round(1000 / fps)

# 비디오 매 프레임 처리
while True:
    ret, frame = cap.read()

    if not ret:
        break

    inversed = ~frame  # 반전

    cv2.imshow("frame", frame)
    cv2.imshow("inversed", inversed)

    if cv2.waitKey(delay) == 27:
        break

cap.release()
cv2.destroyAllWindows()
