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


with serial.Serial ('COM26', 115200) as ser_port:
    
    # ser_port.write (b'0.05\r\n')   # Write bytes, not a string
    # ser_port.write (b'13000\r\n')
   
    #ser_port.write(b'\x04\r\n')
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
x=[]
y=[]          
for n in range (len(data_results)):
    try:
        item=data_results.split(',')
        x.append(float(data_results[n]))
        y.append(float(data_results[n]))
    except ValueError:
        continue
    
# f = open('csv.csv','w')
# writer = csv.writer(f)

# for row in data_results:
#     for n in range (len(data_results)):
#         writer.writerow(data_results[n])

# f.close()

# x_val = [x[0] for x in data_results]
# y_val = [x[1] for x in data_results]


# plt.plot(x_val,y_val)
# plt.plot(x_val,y_val, 'or')

# # Axis Labeling
# plt.xlabel('Time (ms)') 
# plt.ylabel('Encoder Position (ticks)') 
    
# # Graph Title
# plt.title('Lab 2 Plots') 

# plt.show()
