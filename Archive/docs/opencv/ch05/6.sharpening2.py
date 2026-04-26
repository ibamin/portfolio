import sys
import numpy as np
import cv2

src = cv2.imread("ch05/rose.bmp")

if src is None:
    print("Image load failed!")
    sys.exit()

# 색을 변환시 예민하게 데이터를 처리해야할 경우 Y(밝기)Cr(색상)Cb(명암)로 변환하여 데이터를 처리
src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)

# 명암을 출력하여 흑백 이미지 출력
src_f = src_ycrcb[:, :, 0].astype(np.float32)
# 흑백이미지를 가우시안 블러 처리
blr = cv2.GaussianBlur(src_f, (0, 0), 2.0)
# 원본이미지의 밝기를 가우시안 블러 처리한 것에 수식을 적용하여 대치
src_ycrcb[:, :, 0] = np.clip(2.0 * src_f - blr, 0, 255).astype(np.uint8)

dst = cv2.cvtColor(src_ycrcb, cv2.COLOR_YCrCb2BGR)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()

cv2.destroyAllWindows()
