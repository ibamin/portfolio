import picamera

with picamera.PiCamera() as camera:
    camera.rotation = 180
    camera.resolution = (640, 480)
    camera.start_preview()
    camera.start_recording("pi_mov.h264")
    camera.wait_recording(30)
    camera.stop_recording()
    camera.stop_preview()
