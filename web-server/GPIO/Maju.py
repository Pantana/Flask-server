import RPi.GPIO as GPIO
import flask import Flask, render_template

Application = Flask(__name__)
# We're using the physical board pin numbers

GPIO.setmode(GPIO.BCM)

# define which pins we are driving the L298N with

DirectionOnePin = 16

DirectionTwoPin = 18

# Define how we are using these pins

GPIO.setup(DirectionOnePin, GPIO.OUT)

GPIO.setup(DirectionTwoPin, GPIO.OUT)

GPIO.PWM(25, 5)
@application.route('/')
def stop():
    GPIO.output(DirectionTwoPin, GPIO.LOW)
    GPIO.output(DirectionOnePin, GPIO.LOW)
    return '<H2>Motor berenti</H2>'
@application.route('/maju')
def maju():
    GPIO.output(DirectionTwoPin, GPIO.LOW)
    GPIO.output(DirectionOnePin, GPIO.HIGH)
    return '<H2>Motor Maju</H2>'
@application.route('/mundur')
def mundur():
    GPIO.output(DirectionTwoPin, GPIO.HIGH)
    GPIO.output(DirectionOnePin, GPIO.LOW)
    return '<H2>Motor Mundur</H2>'
if __name__ == '__main__':
    application.run(debug=True)
