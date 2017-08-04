import unicornshield as unicorn
from time import sleep
try:
        while True:
                if unicorn.nose() > 0.2:
                        unicorn.setAll(0,0,255)
                        unicorn.show()
                        sleep(1)
                        unicorn.clear()
                        sleep(1)
except:
        unicorn.clear()
