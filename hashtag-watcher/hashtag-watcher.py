import unicornshield as unicorn
from twython import TwythonStreamer
import time

searchTerm = '#WednesdayWisdom'

# Insert your API credentials here
APP_KEY = '...'
APP_SECRET = '...'
OAUTH_TOKEN = '...-...'
OAUTH_TOKEN_SECRET = '...'

# Setup callbacks from Twython Streamer
class BlinkyStreamer(TwythonStreamer):
  def on_success(self, data):
    if 'text' in data:
      print data['text'].encode('utf-8')
      print
      unicorn.setAll(155,0,155)
      unicorn.show()
      time.sleep(1)
      unicorn.clear()

# Create streamer
try:
  stream = BlinkyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
  stream.statuses.filter(track=searchTerm)
except KeyboardInterrupt:
  unicorn.clear()
