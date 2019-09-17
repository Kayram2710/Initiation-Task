import serial
import time

arduinoData = serial.Serial('/dev/ttyUSB0',9600)
time.sleep(2)

print ("Which LED do you want on?")
print ("Type one of the following: 'Red' 'Blue' 'Neither' 'Both'")

while 1:

    var = raw_input()

    if (var == 'Red'):
        arduinoData.write('R')
        time.sleep(1)

    if (var == 'Blue'):
        arduinoData.write('B')
        time.sleep(1)

    if (var == 'Neither'):
        arduinoData.write('O')
        time.sleep(1)

    if (var == 'Both'):
        arduinoData.write('T')
        time.sleep(1)
