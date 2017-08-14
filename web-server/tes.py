import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(13, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

GPIO.output(13, GPIO.HIGH)
GPIO.output(26, GPIO.HIGH)

GPIO.cleanup()
