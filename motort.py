#Import modul time
import time  
#Import modul RPi.GPIO
import RPi.GPIO as GPIO
 
#Set penomeran pin dengan standar Broadcom  
GPIO.setmode(GPIO.BCM)
#Setup Pin PWM
GPIO.setup(25, GPIO.OUT)  
#Setup Pin kontrol maju mundur
GPIO.setup(22, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(26,GPIO.IN, pull_up_down=GPIO.PUD_UP)
p = GPIO.PWM(25, 10)
p.start(5)

while True:
    i = GPIO.input(26)
    if i == True:
        print ("Tombol Aktif")
        GPIO.output(22, GPIO.LOW)
        GPIO.output(27, GPIO.HIGH)

    else:
        print ("Tombol NonAktif")
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(27, GPIO.LOW)
            
GPIO.cleanup()
