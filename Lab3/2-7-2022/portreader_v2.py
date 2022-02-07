"""
    @file                    EncoderDriver.py
    @author                  Daniel Gonzalez
    @author                  Nolan Clapp
    @author                  Caleb Kephart
    @date                    January 31, 2022
"""
import csv
import time
import serial 
from matplotlib import pyplot as plt


with serial.Serial ('COM6', 115200) as ser_port:
    
    ser_port.write (b'0\r\n')
    time.sleep(1)
    ser_port.write(b'\x03')
    data_results=[]
    while True :
        try:
            line = ser_port.readline().strip().decode()
            print (line)
            data_results.append(line)
            if line == 'Stop Data':

                raise KeyboardInterrupt    
        except KeyboardInterrupt:
            break
        

data_results = ','.join(data_results).split(',')
print(data_results)   

   
# item_x = [i.split(',', 1)[0] for i in data_results]
# print(item_x)        
   
# item_y = [i.split(',', 1)[0] for i in data_results]
# print(item_y)  
# 

# plt.plot(item_x,item_y)
# plt.plot(item_x,item_y, 'or')

# # Axis Labeling
# plt.xlabel('Time (ms)') 
# plt.ylabel('Encoder Position (ticks)') 
    
# # Graph Title
# plt.title('Lab 3 Plots') 

# plt.show()

