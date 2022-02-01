"""
    @file                    EncoderDriver.py
    @author                  Daniel Gonzalez
    @author                  Nolan Clapp
    @author                  Caleb Kephart
    @date                    January 31, 2022
"""

import time
import serial 
from matplotlib import pyplot as plt


with serial.Serial ('COM6', 115200) as ser_port:
    
    ser_port.write (b'0.05\r\n')   # Write bytes, not a string
    ser_port.write (b'13000\r\n')
   
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
            
data_results = 

x_val = [x[0] for x in data_results]
y_val = [x[1] for x in data_results]


plt.plot(x_val,y_val)
plt.plot(x_val,y_val, 'or')

# Axis Labeling
plt.xlabel('Time (ms)') 
plt.ylabel('Encoder Position (ticks)') 
    
# Graph Title
plt.title('Lab 2 Plots') 

plt.show()