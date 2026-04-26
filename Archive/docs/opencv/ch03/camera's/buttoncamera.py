import picamera
import time
import RPi.GPIO as GPIO
from datetime import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
sensor = 17

i = 0


def take_picture(channel):
    global i
    with picamera.PiCamera() as camera:
        GPIO.setup(15, 0)
        camera.rotation = 180
        camera.resolution = (640, 480)
        camera.start_preview()
        camera.image_effect = "sketch"
        GPIO.setup(18, 1)
        time.sleep(3)
        GPIO.setup(18, 0)
        name = "pi_still_" + str(i) + ".jpg"
        camera.capture(name)
        camera.stop_preview()
        i += 1
        print(name + "사진 촬영 완료")
        GPIO.setup(15, 1)


def take_picture1():
    global i
    with picamera.PiCamera() as camera:
        GPIO.setup(15, 0)
        camera.rotation = 180
        camera.resolution = (640, 480)
        camera.start_preview()
        camera.image_effect = "sketch"
        GPIO.setup(18, 1)
        time.sleep(3)
        GPIO.setup(18, 0)
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        name = str(formatted_time)
        camera.capture(name + ".jpg")
        camera.stop_preview()
        i += 1
        print(name + "사진 촬영 완료")
        GPIO.setup(15, 1)


GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(15, 1)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, 0)
GPIO.setup(sensor, GPIO.IN)
GPIO.add_event_detect(14, GPIO.RISING, callback=take_picture, bouncetime=300)

while True:
    if GPIO.input(sensor) == 1:
        take_picture1()
    time.sleep(1.5)
