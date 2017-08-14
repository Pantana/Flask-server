from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        i = GPIO.input(26)
        if i == False:
            print ("Tombol Aktif")
        else:
            print ("Tombol NonAktif")
finally:
    GPIO.cleanup()
