# Raspberry Pi 3 GPIO Pins Status And Control Using Flask Web Server and Python

import RPi.GPIO as GPIO
import time
from flask import Flask, render_template, request
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

ledRed1 = 21
ledYellow1 = 20
ledGreen1 = 16

ledRedSts1 = 0
ledYellowSts1 = 0
ledGreenSts1 = 0

ledRed2 = 26
ledYellow2 = 19
ledGreen2 = 13

ledRedSts2 = 0
ledYellowSts2 = 0
ledGreenSts2 = 0

GPIO.setup(ledRed1, GPIO.OUT)
GPIO.setup(ledYellow1,GPIO.OUT)
GPIO.setup(ledGreen1, GPIO.OUT)
GPIO.output(ledRed1, GPIO.LOW)
GPIO.output(ledYellow1, GPIO.LOW)
GPIO.output(ledGreen1, GPIO.LOW)

GPIO.setup(ledRed2, GPIO.OUT)
GPIO.setup(ledYellow2,GPIO.OUT)
GPIO.setup(ledGreen2, GPIO.OUT)
GPIO.output(ledRed2, GPIO.LOW)
GPIO.output(ledYellow2, GPIO.LOW)
GPIO.output(ledGreen2, GPIO.LOW)

@app.route('/')
def index():
    ledRedSts1 = GPIO.input(ledRed1)
    ledYellowSts1 = GPIO.input(ledYellow1)
    ledGreenSts1 = GPIO.input(ledGreen1)
    ledRedSts2 = GPIO.input(ledRed2)
    ledYellowSts2 = GPIO.input(ledYellow2)
    ledGreenSts2 = GPIO.input(ledGreen2)
    templateData = {
    'ledRed1' : ledRedSts1,
    'ledYellow1' : ledYellowSts1,
    'ledGreen1' : ledGreenSts1,
    'ledRed2' : ledRedSts2,
    'ledYellow2' : ledYellowSts2,
    'ledGreen2' : ledGreenSts2 }
    return render_template('index.html', **templateData)
@app.route('/<deviceName>/<action>')
def do(deviceName, action):
    if deviceName == "ledRed1":
        actuator = ledRed1
    if deviceName == "ledYellow1":
        actuator = ledYellow1
    if deviceName == "ledGreen1":
        actuator = ledGreen1
    if deviceName == "ledRed2":
        actuator = ledRed2
    if deviceName == "ledYellow2":
        actuator = ledYellow2
    if deviceName == "ledGreen2":
        actuator = ledGreen2
    if action == "on":
        GPIO.output(actuator, GPIO.HIGH)
        if actuator == ledRed1:
            GPIO.output(ledGreen2, GPIO.HIGH)
        if actuator == ledGreen1:
            GPIO.output(ledRed2, GPIO.HIGH)
    if action == "off":
        GPIO.output(actuator, GPIO.LOW)
    ledRedSts1 = GPIO.input(ledRed1)
    ledYellowSts1 = GPIO.input(ledYellow1)
    ledGreenSts1 = GPIO.input(ledGreen1)
    
    ledRedSts2 = GPIO.input(ledRed2)
    ledYellowSts2 = GPIO.input(ledYellow2)
    ledGreenSts2 = GPIO.input(ledGreen2)
    
    templateData = {
    'ledRed1' : ledRedSts1,
    'ledYellow1' : ledYellowSts1,
    'ledGreen1' : ledGreenSts1,
    'ledRed2' : ledRedSts2,
    'ledYellow2' : ledYellowSts2,
    'ledGreen2' : ledGreenSts2 }
    
    return render_template('index.html', **templateData )

if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug=True)

