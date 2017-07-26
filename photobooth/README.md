# Coding Unicorn Shield Photobooth

![Coding Unicorn Shield Photobooth in action](img/coding_unicorn_shield_photoboth.gif)

In this project we will build a small photo booth that takes pictures after touching the unicorn nose. The LEDs on the Unicorn will be used as countdown element and as indicator if the image was successfully saved.

## What you need

For this you need:
1. A running Rasbpberry Pi (we choose the B3)
2. Raspberry Pi Camera Module
3. Your Coding Unicorn Shield


## Get started
If you have never worked with the Raspberry Pi Camera Module and Python, the Raspberry Pi Foundation has an good introduction for this [here](https://www.raspberrypi.org/learning/getting-started-with-picamera/) you can find our  [german translation here](https://codingworld.io/project/die-raspberry-pi-kamera-benutzen).

You can activate the camera module with `sudo raspi-config` and then `5 Interfacing Options -> P1 Camera -> Yes -> Ok` and then restarting your Raspberry Pi.
After this you should connect your unicorn Shield to the Raspberry Pi and also connect the Camera.

[**photobooth.py**](photobooth.py)

## The Code
```python
from picamera import PiCamera
import unicornshield as unicorn
import time

camera = PiCamera()

camera.start_preview() # starting the preview
try:
  while True:
    unicorn.setAll(0,255,0)
    unicorn.show()

    if unicorn.nose() > 0.2:
      for x in range(9):
          unicorn.setPixel(x,255,0,255)
          unicorn.show()
          time.sleep(0.3)

      camera.capture('/home/pi/Desktop/'+str(time.time())+'.jpg')
      unicorn.setAll(0,0,255)
      unicorn.show()
      time.sleep(2)
except:
  camera.stop_preview() # ending the preview
  unicorn.clear()

```

After starting the program you can always stop it with `Ctrl + c` on your keyboard. To see the preview image you need to connect a display to the raspberry pi, but the program will work also without a connected display.
The program will show you with the green light that it is ready to take the picture. After touching the nose, we can see the countdown because more of the led get to pink. After the picture was taken the whole unicorn shield will be blinking in blue to display that the image was taken and then change back into green so you know, the program is ready to take another picture. You always can change the color of the LEDs so that the unicorn can use your favorite colors.

##
In the first three lines of the code we are just including the necessary libraries. This is `PiCamera` for the camera, `unicornshield` for the Coding Unicorn Shield and `time`.

In line 5 we are creating a variable with the name *camera* and start in line 7 the preview for the camera. In line 8 to 25 we have a while loop in a try statement. We are using the try statement so we can have control what happens then the program is closed with `Control + C`. In this case the lines 24 and 25 will be executed. In this lines we are stopping the preview and turn off all the lights on the Coding Unicorn Shield.

In line 9 we have a while loop which is always running, so we can can continue forever with taking pictures. In line 10 and 11 we are turning all the RGB LEDs on the Coding Unicorn Shield on. We can do this with `unicorn.setAll()` and then give this function the rgb colors as variables. We can use for every color (red, green, blue) parameters from 0 to 255. Because we want to set the color to green, we use 255 as second parameter. In line 11 we are showing this on the Unicorn Coding Shield.

In line 13 we have the main part. With this if condition we are testing if the nose/the light dependent resistor of the Unicorn Shield was touched. If this is the case the intended block starting in line 14 to 22 will be executed.

This block starts with the countdown animation. For this we are creating a small for loop in line 14 which then turns on every RGB LED. For this we are using the function `.setPixel()` in line 15. This function is quite similar to `.setAll()` with the difference that we have 4 parameters. The first parameter is for the position of the pixel. This can be 0 for first (placed on the left foot) or 8 for the last (which is located on the top of the horn). The following parameters are for the rgb values.
In line 17 we are taking a small break after turning on a single led. So by the end of the for loop, the user had about 2,7 seconds to make a pretty face. If you think this time is to short or to long, you always can change the parameter in line 17.

In line 19 we are taking finally taking the picture. For this we use the `.capture()` function. This function has just one parameter and this is the path and name for saving the image. If we always use the same path and name, the image will be overridden. That's why we use `+str(time.time())+`. This will give the image the name of the current [unix timestamp](https://en.wikipedia.org/wiki/Unix_time). For short this timestamp is number of seconds since 1st of January 1970. This isn't the nicest number for a picture, but it will do the work.

In line 20 we are using the `.setAll()` function again to make the Unicorn Shield shine blue. This is cool because the users know that the picture was successfully taken. In line 22 is another small break so before the loops starts again in line 10 and makes the RGB LEDs green again for another photo.

 ## Conclusion
 This little project shows how you can connect the input devices for the unicorn and having a pretty smart way in using the RGB LEDs. You also could add further functionality to this project by e.g. tweet the last photo after pressing the button or taking a video and then creating GIF. Like always the possibilities are nearly endless.

![Samuel Brinkmann taking a selfie with the Coding Unicorn Shield](img/picture-raspberrypi-camera.jpg)

 Code - Create - Change
