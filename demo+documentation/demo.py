import unicornshield as unicorn
from time import sleep
from random import randint

while True:
    if unicorn.nose() > 0.3:
        unicorn.clear()
        unicorn.leftEyeOn()
        sleep(0.5)
        unicorn.rightEyeOn()
        sleep(0.5)
        unicorn.leftEyeOff()
        sleep(0.5)
        unicorn.rightEyeOff()

        for x in range(9):
            unicorn.setPixel(x,255,0,255)
            unicorn.show()
            sleep(0.2)
        sleep(2)
        for x in range(9):
            unicorn.setPixel(x,0,0,0)
            unicorn.show()
            sleep(0.1)

    elif unicorn.buttonPressed() == True:
        colors = [0,0,0]
        for x in range(3):
            for y in range(255):
                    colors[x] = y
                    unicorn.setAll(colors[0],colors[1],colors[2])
                    unicorn.show()
                    sleep(0.01)
            colors[x] = 0
            sleep(2)
        unicorn.clear()

    else:
        unicorn.setAll(randint(0,255),randint(0,255),randint(0,255))
        unicorn.show()
