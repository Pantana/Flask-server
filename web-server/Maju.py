import RPi.GPIO as GPIO
from flask import Flask, render_template

application = Flask(__name__)
# We're using the physical board pin numbers
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# define which pins we are driving the L298N with

D1 = 13
D2 = 5

# Define how we are using these pins

GPIO.setup(D1, GPIO.OUT)
GPIO.setup(D2, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

p=GPIO.PWM(25,100)
p.start(10)

@application.route('/')
def stop():
    GPIO.output(D1, GPIO.LOW)
    GPIO.output(D2, GPIO.LOW)
    return '<H1>Motor Berenti</H1>'
@application.route('/maju')
def maju():
    GPIO.output(D1, GPIO.LOW)
    GPIO.output(D2, GPIO.HIGH)
    return '<H1>Motor Maju</H1>'
@application.route('/mundur')
def mundur():
    GPIO.output(D1, GPIO.HIGH)
    GPIO.output(D2, GPIO.LOW)
    return '<H1>Motor Mundur</H1>'
if __name__ == '__main__':
   application.run(host='0.0.0.0', port=80, debug=True)
