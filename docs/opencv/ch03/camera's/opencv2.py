import cv2
import numpy as np
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)


def led(color):
    GPIO.output(14, 0)
    GPIO.output(15, 0)
    GPIO.output(18, 0)
    print(color)
    if color == "red":
        GPIO.output(14, 1)
    elif color == "blue":
        GPIO.output(15, 1)
    elif color == "green":
        GPIO.output(18, 1)


def main():
    camera = cv2.VideoCapture(0)
    camera.set(3, 320)
    camera.set(4, 240)

    while 1:
        _, frame = camera.read()

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_blue = (100, 100, 120)
        upper_blue = (150, 255, 255)

        lower_green = (50, 150, 50)
        upper_green = (80, 255, 255)

        lower_red = (150, 50, 50)
        upper_red = (180, 255, 255)

        redmask = cv2.inRange(hsv, lower_red, upper_red)
        greenmask = cv2.inRange(hsv, lower_green, upper_green)
        bluemask = cv2.inRange(hsv, lower_blue, upper_blue)

        cv2.imshow("Frame", frame)
        cv2.imshow("Red", redmask)
        cv2.imshow("Green", greenmask)
        cv2.imshow("Blue", bluemask)

        redPixels = cv2.countNonZero(redmask)
        greenPixels = cv2.countNonZero(greenmask)
        bluePixels = cv2.countNonZero(bluemask)

        colorlist = [redPixels, greenPixels, bluePixels]
        maxValue = max(colorlist)
        maxPos = colorlist.index(maxValue)
        print("maxVlue : " + str(maxValue))
        if maxValue >= 1000:
            if maxValue == redPixels:
                led("red")
            elif maxValue == bluePixels:
                led("blue")
            elif maxValue == greenPixels:
                led("green")
        else:
            led(" ")

        print(maxValue, maxPos)
        print(redPixels, greenPixels, bluePixels)

        if cv2.waitKey(1) == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
