from time import sleep
import RPi.GPIO as GPIO
from flask import Flask, render_template

application = Flask(__name__)
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.IN, GPIO.PUD_UP)
i = GPIO.input(26)
if i == True:
    @application.route('/')
    def ya():
        return '<h2>ya</h2>'
else:
    @application.route('/tidak')
    def tidak():
        return '<h2>tidak</h2>'
        
if __name__ == '__main__':
   application.run(host='0.0.0.0', port=80, debug=True)
