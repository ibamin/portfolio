import picamera
import time

with picamera.PiCamera() as camera:
    camera.rotation = 180
    camera.resolution = (640, 480)
    camera.start_preview()
    camera.image_effect = "sketch"
    time.sleep(5)
    camera.capture("pi_still.jpg")
    camera.stop_preview()
