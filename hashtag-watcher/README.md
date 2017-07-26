# Coding Unicorn Shield Project: Hashtag Watch

Twitter is a great service for short messages with less than 140 characters. You can follow for example us at [@codingworlden](https://twitter.com/codingworlden) but you also can integrate it easily in your program because of their quiet open API. In this project, we are using their API and are listening to special words which are send. You can easily mark a tweet with a # or hashtag for a topic. With this project we are listening to one hashtag and every time someone is using this hashtag, our Coding Unicorn Shield will blink. In this example we are have listned to [#WednesdayWisdom](https://twitter.com/search?q=%23WednesdayWisdom) but obviously you can look for various content. You can find more information in this [Sparkfun Tutorial])(https://learn.sparkfun.com/tutorials/raspberry-pi-twitter-monitor) and this [Tutorial by the Raspberry Pi Foundation](https://www.raspberrypi.org/learning/getting-started-with-the-twitter-api/worksheet/)

## What you need

For this you need:
1. A running Rasbpberry Pi with an Internet Connection
2. Your Coding Unicorn Shield
3. Twitter Account and APP Credentials ([Click here for a tutorial](create-twitter-api-account.md))

## Needed libraries
For this project to work we need to install the following python libaries on your raspberry pi:


`sudo pip install twython`

 In our case we did also need to install the following libary:

 `sudo pip install requests requests_oauthlib`


## Code

[**hashtag-watcher.py**](hashtag-watcher.py)

```python
import unicornshield as unicorn
from twython import TwythonStreamer
import time

searchTerm = '#WednesdayWisdom'

# Insert your Information here
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
```
`sudo python hastag-watcher.py`

Before starting the program, please use your API credentials in line 8 to 11. Please keep in mind to never pulish them.

## Step for step

In first three lines we are importing all the libaries. We need the `unicornshield` for talking to RGB LEDs on the Unicorn. The `twython` libary is our favorite libary for dealing with the Twitter API. This makes the work really easy like you will see in the program.

In line 5 we defining the variable *serachTerm* and are filling it with a string and in this string we having our hashtg. You can change this to the hashtag of your choice.

In line 7 to 11 we creating variables for the API credentials. Here you need to fill in the credentials which you are created.

The next part is a bit complicated so we will try to give a short but easy conclusion. We are basically creating a new class which is based on the TwythonStreamer class which is part of the Twython libary. A class creates a lot of possible ways to structure your program. We don't need to know so much about the TwythonStreamer class because the only interesting thing for us is the on_success() function. This function is only called, then the search term is found. So every in intened in line 17 to 22 is only executed then the search term is found. In this case we are first of all printing the tweet in line 17 and 18. You don't need this two lines for the blinking unicorn. In line 19 to 22 we are doing the blinking magick. For this we are using the `.setAll()` function with which we can set all the RGB LEDs to one color. In this case we choose purple.
In line 22 we are turning all LEDs off. In line 21 you can change the time of blinking. If you don't have so many hashtags you also can use a longer time of blinking.

We have created now the class, but we didn't implement it. This is hapening in line 25 to 29. We are first of all creating the variable *stream* and filling it with the class BlinkyStreamer. This class uses as parameters the API credentials. You probaly cann already see the connection to the class we created in line 14. With the comand in line 27 we are making sure that the function which we created in line 15 is called if their is the searchTerm we are looking for.
All this is wrapped in a try statement and the program can be closes with `Ctrl + C`

## Conclusion
With this project we can easily visulize the global buzz of social media. We can use this for our own hastags or for displaying hashtags at an event. This is also cool because everyone with a twitter account can make the unicorn blinkg. But it also shows what things we can display with the Coding Unicorn Shield.

Code - Create - Change
