#Name:   PythonWorkshopPrepCode.py
#Author: Joe Haun
#Purpose:The purpose of this code is to test the workshop attendees' systems for proper installation of necessary code.

import serial
import sys

print("Your Operating System: ", sys.platform)
print("Attempting to open a port to test for PySerial Library. If error results, please install or reinstall the library.")
if(sys.platform == 'windows'):
    Port = serial.Serial('COM1');
    Port.close();
else:
    Port = serial.Serial('/dev/tty1');
    Port.close();

print("A port has been opened on your system and you have the PySerial Library installed correctly. You are ready for the workshop.")
