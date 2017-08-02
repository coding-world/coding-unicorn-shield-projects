from flask import Flask, request
from flask_cors import CORS, cross_origin
import json
import unicornshield as unicorn


app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return app.send_static_file('unicorn.txt')

@app.route("/eye/left")
def leftEye():
    status = request.args.get('status')
    if status == None:
        return json.dumps({"status": False, "msg": "You must send >status< via GET Request"})

    if status == "on":
        unicorn.leftEyeOn()
    elif status == "off":
        unicorn.leftEyeOff()
    else:
        return json.dumps({"status": False, "msg": "status must be >on< or >off<"})

    return json.dumps({"status": True});

@app.route("/eye/rigth")
def rightEye():
    status = request.args.get('status')
    if status == None:
        return json.dumps({"status": False, "msg": "You must send >status< via GET Request"})

    if status == "on":
        unicorn.rightEyeOn()
    elif status == "off":
        unicorn.rightEyeOff()
    else:
        return json.dumps({"status": False, "msg": "status must be >on< or >off<"})

    return json.dumps({"status": True});

@app.route("/nose")
def nose():
    return json.dumps({"status": True, "data": unicorn.nose()});

@app.route("/ear")
def ear():
    return json.dumps({"status": True, "data": unicorn.buttonPressed()});

@app.route("/pixel/<id>")
def pixel(id):
    try:
        id = int(id)
    except:
        return json.dumps({"status": False, "msg": "ID must be a integer"});

    if id < 0 or id > 8:
        return json.dumps({"status": False, "msg": "ID not valide (0-8 are valide)"});

    r = request.args.get('r')
    g = request.args.get('g')
    b = request.args.get('b')

    if r == None or g == None or b == None:
        return json.dumps({"status": False, "msg": "You need to send r, g and b via GET parameter"});

    try:
        r = int(r)
        g = int(g)
        b = int(b)
    except:
        return json.dumps({"status": False, "msg": "r, g and b must be integer"});

    if r < 0 or r > 255:
        return json.dumps({"status": False, "msg": "r must between 0 and 255"});
    if g < 0 or g > 255:
        return json.dumps({"status": False, "msg": "g must between 0 and 255"});
    if b < 0 or b > 255:
        return json.dumps({"status": False, "msg": "b must between 0 and 255"});

    unicorn.setPixel(id, r, g, b)
    unicorn.show()

    return json.dumps({"status": True});



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
