import serial
import time
from flask import Flask, render_template, Response, request, redirect, url_for

arduinoData = serial.Serial('/dev/ttyUSB0',9600)
time.sleep(2)

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('layout.html')

@app.route("/Red/", methods=['POST'])
def R():
    arduinoData.write('R')
    time.sleep(1)
    return render_template('layout.html')

@app.route("/Blue/", methods=['POST'])
def B():
    arduinoData.write('B')
    time.sleep(1)
    return render_template('layout.html')

@app.route("/Neither/", methods=['POST'])
def O():
    arduinoData.write('O')
    time.sleep(1)
    return render_template('layout.html')

@app.route("/Both/", methods=['POST'])
def T():
    arduinoData.write('T')
    time.sleep(1)
    return render_template('layout.html')

if __name__ == '__main__':
    app.run()
