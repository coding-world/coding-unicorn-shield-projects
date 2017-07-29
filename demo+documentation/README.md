# Coding Unicorn Shield Demo and Documentation Pi/Python

![Demo Code on Coding Unicorn Shield](img/demo.gif)

Here you see a simple Demonstration with the Coding Unicorn Shield connected to a Raspberry Pi and programmed with Python. You can find out more information on the Kickstarter Page.

## Basics
The Coding Unicorn Shield is an atachable shield for the Raspberry Pi and Arduino. On the frontpage you not only find the image of a cute unicorn but also severall LEDs and Input devices. For Input we can either use the light depedend resistor (the nose) or the button (on the ear). For output we have two 5mm white LEDs. Their are also 9 WS2812B SMD LEDS also called Pixels on the foots, the tail and the horn. These are all already conncted to the GPIO Pins and can be programmed right away.

## What you need

1. Running Raspberry Pi with an internet connection
2. Your Coding Unicorn Shield


## Install the libary and software setup

> Please note that the libary is still under construction

We have created a libary for the Raspberry Pi and Python. You can install it with the following comands:

# Coding Unicorn Shield Python Libary

> Please note: This libary is only a beta!

**Install from Github clone**


```git clone https://github.com/coding-world/unicorn-shield-python```


```cd unicorn-shield-python/```


```sudo apt-get install python-dev python-setuptools```


```cd rpi-ws281x```


```sudo python setup.py install```


```cd ..```


```cd UnicornShield```


```sudo python setup.py install```


```cd ..```




Because the WS2812B/Pixel need the hardware PWM (GPIO18) for their communication, which is also used to generate the audio for the headphone jack, we maybe need to turn that off. You can do that with `sudo raspi-config` and then `7 Advanced Options -> A4 Audio -> 2 Force HDMI -> Ok`.

## List of function
| Function | Explaination | Parameters |
| -- | -- | -- |
| `.brightness(b)` | Set's the brightness for the RGB LED/Pixel on the Unicorn | b=brightness, ranging from 0-1 |
| `.getBrightness()` | Returns the current brightness | |
| `.clear()` | Turns off all the RGB LEDs/Pixels | |
| `.setPixel(x,r,g,b)` | Set the color for one RGB LED/Pixel | x=Position, ranging from 0-8; r=color red, ranging from 0 to 255; g=color green, ranging from 0 to 255; b=color blue, ranging from 0 to 255 |
| `.getPixel(x)` | Get's the current color value | x = Position, ranging from 0 - 8 |
| `.setAll(r,g,b)` | Set one color code for all RGB LEDs/Pixel | r=color red, ranging from 0 to 255; g=color green, ranging from 0 to 255; b=color blue, ranging from 0 to 255  |
| `.show()` | Displays the values set by `.setPixel()` and `.setAll()` on the Shield | |
| Eyes | | |
| `.leftEyeOn` | Turns the LED on the left eye on | |
| `.leftEyeOff` | Turns the LED on the left eye off | |
| `.leftRightOn` |Turns the LED on the right eye on | |
| `.leftRightOff` | Turns the LED on the right eye off | |
| Nose | | |
| `.nose()` | Returns the value of the current brightness. Around 0.3 in room lightning | |
| Button / Ear | | |
| `.buttonPressed()` | Return `False` or `True` if the button on the ear is pressed| |


## The Demo Code

[**demo.py**](demo.py)


```python
import unicornshield as unicorn
from time import sleep
from random import randint

while True:
    print unicorn.buttonPressed()
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
```

## How to execute the program

You can execute the program with `sudo python demo.py` and then stop the program at any time with `Ctrl + C`.  You always need to execute the program with sudo because we need the pwm signals for the Pixels/WS2812B LEDs.

## Step for Step
In the first three lines we are including all the neccassary libaries. We need the `unicornshield` libary which we did install in the steps before. because `unicornshield` is quiet a long name, we use the `as unicorn` for giving it a short nickname. For making our animation more beautial we also use the `sleep()`
function from the `time` libary and the `randint()` function from the `random` libary.

The whole program is in an while loop that begins in line 5 and is always true, so it is running till the program is stopped.

Inside the while loop we have in line 6, 26 and 38 an if statement with 3 different possibilits. The first one is checked in line 6 and is true if the value from `.nose()` is less than *0.3* this is usually the case if someone holds their finger, with normal room lighting, above the sensor. If this case is true, the intended block from line 7 to line 24 will be executed.

In line 7 we are first of all making sure that all the Pixels are turned off, for this we can easily use the `.clear()`.
In the first part from line 8 to line 14 we are turning on the Eye LEDs and then turning them off. For this we are using e.g. `leftEyeOn()` or `.leftEyeOff()`. With the `.sleep()` function, we can make the whole process more pretty.

In line 16 to 24 we are creating a animation with the Pixels/RGB LEDs. For this we use a foor loop to turn on every pixel indiviudally. With `.setPixel()` we can give each Pixel a certain color. The first parameter is the position of the pixel. This is defined with the help of the for loop. The next parameters are for the color. With: 255,0,255 , we are creating the color purple. With the `.show()` function, we are putting this colors on the Pixels. If we don't use this function, the Pixel won't change it color. The `sleep(0.2)` function in line 19 enables us to see the LED's filling up.
In line 21 to 24 we are doing the exact opposite. We are turning one by one pixel off. For this we also can use the `.setPixel()` function. This we just use 0 for all the colors. Because the pixel can't display black light, black is just the turned off pixel.

In line 26 we have a elif condition. This condition is only checked when the the first if conditon in line 6 was false. This condition is correct then `.buttonPressed()` is True and everything from line 27 to 36 are executed. This means that the button on the ear of the unicorn is pressed. In this examples we want to further display the RGB-Color System. RGB is short for Red, Green and Blue. With this colors we can in theory build every color like: purple, yellow or green. You can find online a lot of color pickers white. http://color-picker.appsmaster.co/. Our company green is btw: 0, 255, 150. But in this example we don't want to mix colors but show the brightness of different colors.
For this we are creating a list with the name *colors* in line 27. In the next line we are creating a for loop, which just helps us to execute the intended code block three times. This is really handy because we want to display the color for red, green and blue.
In the next line another for loop starts, but this foor loop does count to 255. This is the maximum we can display for one color. Because we wanted to save code and only display one color at the time, we are saving the current value of *y* in the list of colors with the number of the color (colors[1] would be green). In the next step we are using the `.setAll()` function. This function has unlike the `.setPixel()` function only three parameters. We don't need to define the positon of the pixel because we are giving all the pixels on the Coding Unicorn Shield the same color. The only three parameters are for red, green and blue. Here are we using the list *colors*. In the next two lines, we are putting the this pixels in action and are using a really short `sleep(0.01)`. In the end of every of the three loops, we are setting the color which was used in line 33 to zero.
In the end of this whole block, we are turning of every color in line 36.

The last part is in the else statement. Which statement and the intendet block is only called then the previous two if stements in line 6 and 26 their booth false. In this case we just want to show some random art. So we are using the `.setAll()` function again but this time we don't define the colors by ourself. With the `randint()` function we can create a random number. With `randint(0,255)` we are creating a random number between 0 and 255. Because this are the maximal and minimal numbers for the parameters we can create some random art which is always changing and with the `.show()` function in the next line, we are putting this random color on the Shield.


## Conlcusion
This demo is short program which shows the most interesting functionality of the Coding Unicorn Shield and how it can be programmed with python. Esspacially the combination of the input devices and the LEDs can improve many projects. The Cute unicorn look is also huge bonus esspecially with non technical people. Please note that this is not final documentation and we will improve all of it in the next movements.

Code - Create - Change
