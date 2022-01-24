# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 18:57:46 2022

@author: Daniel Ceja Gonzalez
        ME 405 
        Homework 0
"""

from matplotlib import pyplot as plt

filename = 'eric.csv'

# Opens file 
with open(filename, 'r') as f:
                data_results = []
                for line in f:
                    item = line.split(',')
                    # Check for valid data
                    try:
                        float(item[0])
                        float(item[1])
                    except ValueError:
                        continue
                    data_results.append((float(item[0]),float(item[1]))) 

                print(data_results)
                        
# PLots first two columns of data                         
x_val = [x[0] for x in data_results]
y_val = [x[1] for x in data_results]


plt.plot(x_val,y_val)
plt.plot(x_val,y_val, 'or')

# Axis Labeling
plt.xlabel('x - axis') 
plt.ylabel('y - axis') 
    
# Graph Title
plt.title('eric.csv Plot') 

plt.show()
