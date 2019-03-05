import picamera
import time

def record(filename = "test.h264"):
    camera = picamera.PiCamera()
    camera.vflip(True)
    camera.start_recording(filename)
    camera = picamera.PiCamera()
    camera.vflip(True)
    camera = picamera.stop_recording

def photo():
    camera = picamera.PiCamera()
    camera.vflip(True)
    camera.capture('test.jpg')
