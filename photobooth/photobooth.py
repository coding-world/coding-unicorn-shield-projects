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
