import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pins=[17,27,23,22,24,25,5,6,12,16]

def blink(pin, t=0.5):
    print ("LED on", pin)
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(t)
    print ("LED off", pin)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(t)

for pin in pins:
    GPIO.setup(pin,GPIO.OUT)

while(True):
    for pin in pins:
        blink(pin,0.1)