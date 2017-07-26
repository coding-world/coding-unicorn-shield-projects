import unicornshield as unicorn
import requests
from time import sleep
from random import randint

url = "http://api.open-notify.org/astros.json"

def displayPoepleInSpace():
  unicorn.clear()
  for i in range(9):
    unicorn.setPixel(i, randint(0,255),randint(0,255),randint(0,255))
    unicorn.show()
    sleep(0.3)
  r = requests.get(url)
  j = r.json()
  n = j['number']
  unicorn.clear()
  for i in range(n):
    unicorn.setPixel(i, 0,0,255)
    unicorn.show()

displayPoepleInSpace()

try:
  while True:
    if unicorn.nose() > 0.2:
      displayPoepleInSpace()
except:
  unicorn.clear()
