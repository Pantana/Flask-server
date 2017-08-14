import RPi.GPIO as GPIO
import time
# We're using the physical board pin numbers

GPIO.setmode(GPIO.BCM)

# define which pins we are driving the L298N with

DirectionOnePin = 16

DirectionTwoPin = 21

# Define how we are using these pins

GPIO.setup(DirectionOnePin, GPIO.OUT)

GPIO.setup(DirectionTwoPin, GPIO.OUT)


#print "Motor A Direction one"
GPIO.output(DirectionOnePin, GPIO.HIGH)

time.sleep(2)

GPIO.output(DirectionOnePin, GPIO.LOW)

#print "Motor A Direction two"
GPIO.output(DirectionTwoPin, GPIO.HIGH)

time.sleep(2)

GPIO.output(DirectionTwoPin, GPIO.LOW)

# This command clears the configuration from the GPIO interface
GPIO.cleanup()
