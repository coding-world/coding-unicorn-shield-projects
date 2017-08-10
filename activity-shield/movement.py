import RPi.GPIO as GPIO
import time
import unicornshield as unicorn
from signal import pause
from gpiozero import Button
from signal import pause

## Reset Funktion, 
def reset():
        global starttime
        starttime = time.time()
        print "Reset"
        unicorn.clear()

button = Button(16)
button.when_pressed = reset

## IR Sensor
SENSOR_PIN = 8
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

## Getting the current timestamp
starttime = time.time()


def move_callback(channel):
        ## Calculating the minutes
        sitting = (time.time() - starttime) / 60 / 5
        print sitting
        
        ## Set all LEDs to RED IF sitting > 9 = 45 min activity 
        if sitting > 9:
                sitting = 9

                unicorn.setAll(0,255,0)
                unicorn.show()
                button.wait_for_press()


		## tun on LEDs acording to sitting (minutes)
        for i in range (0, int(sitting)):
                unicorn.setPixel(i,155,0,0)
        print('Movement detected')
        unicorn.show()
    



try:
    GPIO.add_event_detect(SENSOR_PIN , GPIO.RISING, callback=move_callback)
    while True:
        time.sleep(180)
        starttime = time.time()
        print "no movement, timer resettet"
        unicorn.clear()
except KeyboardInterrupt:
    print "Stop"
GPIO.cleanup()
