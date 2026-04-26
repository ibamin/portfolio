import cv2
import numpy as np
import random
import time  # time 모듈 추가

thresh = 25
max_diff = 5


def dice_shake():
    dices = []
    a, b, c = None, None, None
    cap = cv2.VideoCapture(cv2.CAP_DSHOW + 0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)
    cup = cv2.imread("Yachu_project/images/cup.png")

    no_motion_time = 0  # 움직임이 없는 시간을 추적하는 변수

    if cap.isOpened():
        ret, a = cap.read()
        ret, b = cap.read()
        while ret:
            ret, c = cap.read()
            if not ret:
                break
            a_gray = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
            b_gray = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
            c_gray = cv2.cvtColor(c, cv2.COLOR_BGR2GRAY)
            diff1 = cv2.absdiff(a_gray, b_gray)
            diff2 = cv2.absdiff(b_gray, c_gray)
            ret, diff1_t = cv2.threshold(diff1, thresh, 255, cv2.THRESH_BINARY)
            ret, diff2_t = cv2.threshold(diff2, thresh, 255, cv2.THRESH_BINARY)
            diff = cv2.bitwise_and(diff1_t, diff2_t)
            k = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
            diff = cv2.morphologyEx(diff, cv2.MORPH_OPEN, k)
            diff_cnt = cv2.countNonZero(diff)

            if diff_cnt > max_diff:
                for i in range(5):
                    r = random.randint(1, 6)  # 주사위 값은 1부터 6까지의 정수
                    if len(dices) != 5:
                        dices.append(r)
                    else:
                        dices[i] = r
                print(dices)

                # 움직임이 감지되면 움직임이 없는 시간 초기화
                no_motion_time = 0
            else:
                # 움직임이 없을 때 움직임이 없는 시간 증가
                no_motion_time += 1

            # 움직임이 없는 시간이 300프레임(약 3초) 이상일 경우 종료
            if no_motion_time > 100:
                print("over time out")
                break

            a = b
            b = c
            if cv2.waitKey(1) & 0xFF == 27:
                break
    cap.release()
    cv2.destroyAllWindows()
    return dices
