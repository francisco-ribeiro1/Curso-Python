#import RPi.GPIO as GPIO
from time import sleep
from picamera import PiCamera
from datetime import datetime
from gpiozero import Button, LED
from signal import pause
import sys

ledGreen = LED(18)
ledRed = LED(17)

cam_button = Button(22)
#out_button = Button(23)

camera = PiCamera(resolution=(2592, 1944))
ledGreen.on()
ledRed.off()

def capture():
	ledGreen.off()
	ledRed.on()
	timestamp = datetime.now().isoformat()
	camera.capture('/home/pi/Workspace/%s.png' % timestamp)
	ledGreen.on()
	ledRed.off()



cam_button.when_pressed = capture
#out_button.when_pressed = sys.exit(0)
pause()

print("Ok")
print("By!")
