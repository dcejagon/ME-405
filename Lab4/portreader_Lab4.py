"""
    @file                    portreader_Lab4.py
    @author                  Daniel Gonzalez
    @author                  Nolan Clapp
    @author                  Caleb Kephart
    @date                    February 14, 2022
    @brief                   Python code that runs on PC while code is running on nucleo. Used to read from the port to collect relevant data and handle such as generating plots.
"""

import time
import serial 
from matplotlib import pyplot as plt


with serial.Serial ('COM26', 115200) as ser_port:
    ## @brief enters 0 for the input to run the rest of the code on nucleo.
    ser_port.write (b'0\r\n')
    time.sleep(5)
    ## @brief enters keyboard interrupt ctrl + c to end code on nucleo
    ser_port.write(b'\x03')
    ## @brief empty array to collect data.
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


## @brief removes unwanted strings from array to allow for plot generation
data_results.pop(len(data_results)-1)
## @brief removes unwanted strings from array to allow for plot generation
data_results.pop(0)

## @brief converts remaining data strings into integers to generate cleaner and more accurate plots.
for i in range(0, len(data_results)):
   data_results[i] = int(data_results[i])
## @brief The time over which data was collected. Estimated to be collecting data about once every millisecond.
Time = range(0,len(data_results))


plt.scatter(Time,data_results)
plt.plot(Time,data_results)

# Axis Labeling
plt.xlabel('Time (ms)') 
plt.ylabel('ADC Step Response (ticks)') 
    
# Graph Title
plt.title('Lab 4 Plots') 
plt.savefig('RC_Circuit_Responce2.png')
plt.show()

