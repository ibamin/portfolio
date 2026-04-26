import easyocr
import matplotlib.pyplot as plt
import cv2

reader = easyocr.Reader(["ko", "en"])
img_path = "ch09/04.png"
img = cv2.imread(img_path)
result = reader.readtext(img_path)
print(result)
THRESHOLD = 0.3
for bbox, text, conf in result:
    if conf > THRESHOLD:
        print(text)
        # cv2.rectangle(img, pt1 = bbox[0], pt2 = bbox[2], color = (0, 0, 255), thickness = 3)

        cv2.rectangle(
            img,
            pt1=(int(bbox[0][0]), int(bbox[0][1])),
            pt2=(int(bbox[2][0]), int(bbox[2][1])),
            color=(0, 0, 255),
            thickness=3,
        )
plt.figure(figsize=(8, 8))
plt.imshow(img[:, :, ::-1])
plt.axis("off")
plt.show()
