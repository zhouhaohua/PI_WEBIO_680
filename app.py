# Raspberry Pi 3 GPIO Pins Status And Control Using Flask Web Server and Python

import time
import RPi.GPIO as GPIO
import time
from flask import Flask, render_template, request
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
ledRed = 13
ledYellow= 19
ledGreen= 26
ledList=[ledRed, ledYellow, ledGreen]
ledRedSts = 0
ledYellowSts = 0
ledGreenSts = 0
GPIO.setup(ledRed, GPIO.OUT)
GPIO.setup(ledYellow,GPIO.OUT)
GPIO.setup(ledGreen, GPIO.OUT)
GPIO.output(ledRed, GPIO.LOW)
GPIO.output(ledYellow, GPIO.LOW)
GPIO.output(ledGreen, GPIO.LOW)
@app.route('/')
def index():
    ledRedSts = GPIO.input(ledRed)
    ledYellowSts = GPIO.input(ledYellow)
    ledGreenSts = GPIO.input(ledGreen)
    templateData = { 'ledRed' : ledRedSts,
    'ledYellow' : ledYellowSts,
    'ledGreen' : ledGreenSts }
    return render_template('index.html', **templateData)
@app.route('/selftest')
def selftest():
    for led in ledList:
        GPIO.output(led, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(led, GPIO.LOW)
    GPIO.output(ledList, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(ledList, GPIO.LOW)
    ledRedSts = GPIO.input(ledRed)
    ledYellowSts = GPIO.input(ledYellow)
    ledGreenSts = GPIO.input(ledGreen)
    selftestres = 1
    templateData = { 'ledRed' : ledRedSts,
    'ledYellow' : ledYellowSts,
    'ledGreen' : ledGreenSts,
    'selftestres': selftestres}
    return render_template('index.html', **templateData)
@app.route('/<deviceName>/<action>')
def do(deviceName, action):
    if deviceName == "ledRed":
        actuator = ledRed
    if deviceName == "ledYellow":
        actuator = ledYellow
    if deviceName == "ledGreen":
        actuator = ledGreen
    if action == "on":
        GPIO.output(actuator, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(actuator, GPIO.LOW)
    if action == "off":
        GPIO.output(actuator, GPIO.LOW)
    ledRedSts = GPIO.input(ledRed)
    ledYellowSts = GPIO.input(ledYellow)
    ledGreenSts = GPIO.input(ledGreen)
    templateData = { 'ledRed' : ledRedSts,
    'ledYellow' : ledYellowSts,
    'ledGreen' : ledGreenSts }
    return render_template('index.html', **templateData )
if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug=True)
