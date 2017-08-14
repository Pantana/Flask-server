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
 
#Maju
#GPIO.output(22, GPIO.HIGH)
#GPIO.output(27, GPIO.LOW)  
 
#Mundur
GPIO.output(22, GPIO.LOW)
GPIO.output(27, GPIO.HIGH)  
 
#Buat instansiasi pin PWM, jika menggunakan dua motor
#namannya bisa diubah menjadi p1 atau p2, bisa juga motor1 dan motor2
p = GPIO.PWM(25, 10)

try:
    p.start(5)
    
except KeyboardInterrupt:
    #Stop penggunaan pwm
    p.stop()
    #Reset gpio dan keluar dari program
    GPIO.cleanup()
