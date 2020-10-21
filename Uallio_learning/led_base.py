import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

WHITE = 2
YELLOW = 3
RED = 4

GPIO.setup(WHITE,GPIO.OUT)
GPIO.output(WHITE,0)
GPIO.setup(YELLOW,GPIO.OUT)
GPIO.output(YELLOW,0)
GPIO.setup(RED,GPIO.OUT)
GPIO.output(RED,0)
class ledc:
    def WHITE():
        GPIO.output(WHITE,1)
        GPIO.output(YELLOW,0)
        GPIO.output(RED,0)

    def YELLOW():
        GPIO.output(WHITE,0)
        GPIO.output(YELLOW,1)
        GPIO.output(RED,0)

    def RED():
        GPIO.output(WHITE,0)
        GPIO.output(YELLOW,0)
        GPIO.output(RED,1)
