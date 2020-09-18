import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

for i in range(10):
	print(i+1, "-  ")
	GPIO.output(18, GPIO.HIGH)
	GPIO.output(17, GPIO.LOW)
	print("Green Led is ON")
	print("Red Led is OFF")
	time.sleep(3)
	
	GPIO.output(18, GPIO.LOW)
	GPIO.output(17, GPIO.HIGH)
	print("Green Led is OFF")
	print("Red Led is ON")
	time.sleep(3)

GPIO.output(17, GPIO.LOW)
GPIO.output(18, GPIO.LOW)
print("By!")

