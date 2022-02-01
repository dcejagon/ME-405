"""
    @file                    EncoderDriver.py
    @author                  Daniel Gonzalez
    @author                  Nolan Clapp
    @author                  Caleb Kephart
    @date                    January 31, 2022
"""

import time
import serial 


with serial.Serial ('COM3', 115200) as ser_port:
    
    ser_port.write (b'0.05\r\n')   # Write bytes, not a string
    ser_port.write(b'13000\r\n')
   
    time.sleep(1)
    
    ser_port.write(b'\x03')
    
    while True :
        try:
            line = ser_port.readline().strip().decode()
            print (line)
            if line == 'Stop Data':
            
                raise KeyboardInterrupt    
        except:
            break
            