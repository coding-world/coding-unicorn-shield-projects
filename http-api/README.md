# Install
First install the Coding Unicorn Shield lib from https://github.com/coding-world/unicorn-shield-python

Install the Requirements via pip by calling:
```
pip install -r requirements.txt
```

# Start HTTP Server
The Server is a small Flask application. You can easy start it with the following command:

```
sudo python server.py
```

# Usage
You can send HTTP Request to the Server (default: http://127.0.0.1:5000)

* /eye/left?status=on -> Turns the left eye on
* /eye/left?status=off -> Turns the left eye off
* /eye/right?status=on -> Turns the right eye on
* /eye/right?status=off -> Turns the right eye off
* /nose -> Return the Value of the Nose-Sensor in Secounds
* /ear -> Return the Value of the Button at the ear of the unicorn
* /pixel/<id>?r=0&g=0&b=0 -> Set one Pixel (relplace <id> with a number from 0 to 8). r, g and b can be between 0 and 255

# Example
Turn the secound Pixel to red:
```
curl "http://localhost:5000/pixel/2?r=255&g=0&b=0"
```
Response:
```
{"status": true}
```

# Response
The Respons is always a json object. It contains the following Attributs:

* status
The Status atribut is always there and contains True or False.
* msg
If the Status is false it contains a error message
* data
At the /nose and /ear request it returns the value from the sensor.

# Mock / Test Version
If you want to run the HTTP Server to test your software but without connect a unicorn you can replace the line

```
import unicornshield as unicorn
```

with

```
from src.unicornMock import unicornmock as unicorn
```

In this case the Server response with some default values and you can develop your own Software to use this API.
