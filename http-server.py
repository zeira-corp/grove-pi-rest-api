#!/usr/local/bin/python
# coding: utf-8
import time
import sys
sys.path.insert(0, '../noob')
from noob import *

from flask import Flask, request, jsonify
app = Flask(__name__)

whiteLed = Led().initialize({
  'name': "WhiteLed",
  'digitalPort': 2,
  'pinMode': "OUTPUT"
})

blueLed = Led().initialize({
  'name': "BlueLed",
  'digitalPort': 3,
  'pinMode': "OUTPUT"
})

redLed = Led().initialize({
  'name': "RedLed",
  'digitalPort': 4,
  'pinMode': "OUTPUT"
})

lcdDisplay = LCDDisplay().initialize({
  'name': "MyDisplay",
  'message': "BoB|SnowCamp"
})

ultrasonicRanger = UltrasonicRanger().initialize({
  'name': "Ranger",
  'digitalPort': 7
})

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/scout/range',methods = ['GET'])
def scout_range():
    return jsonify({"range":ultrasonicRanger.distance()})

@app.route('/led/<color>/blink',methods = ['GET'])
def led_blink(color):
    if color == 'white':
        #lcdDisplay.setRGB(255,255,255)
        #lcdDisplay.setText("White").console()
        whiteLed.blink(0.5)
    elif color == 'blue':
        #lcdDisplay.setRGB(0,0,255)
        #lcdDisplay.setText("Blue").console()
        blueLed.blink(0.5)
    elif color == 'red':
        #lcdDisplay.setRGB(255,0,0)
        #lcdDisplay.setText("Red").console()
        redLed.blink(0.5)
    else:
        print('😡 Houston, we have a problem')
    #return '%s led blink' % color
    return jsonify({"color":color})

@app.route('/lcd',methods = ['POST'])
def lcd_display():
    lcdDisplay.setRGB(255,255,0)
    content = request.json
    lcdDisplay.setText(content['message']).console()
    return jsonify({"message":content['message']})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8085, debug=True)

 #sudo python http-server.py
