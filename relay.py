from time import sleep
import RPi.GPIO as GPIO

pin1 = 23
pin2 = 8
pin3 = 25
pin4 = 24

flash = .1

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)
GPIO.setup(pin4, GPIO.OUT)



while True:
        
	GPIO.output(pin1, False)
	sleep(flash)
        GPIO.output(pin2, False)
        sleep(flash)
	GPIO.output(pin3, False)
        sleep(flash)
	GPIO.output(pin4, False)
	sleep(flash)




	GPIO.output(pin1, True)
	GPIO.output(pin2, True)
	GPIO.output(pin3, True)
	GPIO.output(pin4, True)
	sleep(flash)		
