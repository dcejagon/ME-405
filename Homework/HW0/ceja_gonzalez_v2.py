# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 10:37:22 2022

@author: dceja
"""

from matplotlib import pyplot as plt

filename = 'test.csv'

with open(filename, 'r') as f:
                data_results = []
                for line in f:
                    item = line.split(',')
                    try:
                        n = 0
                        while(n < 2):
                           x = None
                           y = None
                           ind = 0
                           
                           if not item[ind]:
                               ind += 1
                           elif(x is None):
                               x = ind
                               n += 1
                           else:
                               y = ind
                               n += 1
                               float(item[x])
                               float(item[y])
                    except ValueError:
                        continue
                
                data_results.append((float(item[x].strip()),float(item[y].strip())))
                                    
# x_val = [x[0] for x in data_results]
# y_val = [x[1] for x in data_results]


# plt.plot(x_val,y_val)
# plt.plot(x_val,y_val, 'or')

# # Axis Labeling
# plt.xlabel('x - axis') 
# plt.ylabel('y - axis') 
    
# # Graph Title
# plt.title('eric.csv Plot') 

# plt.show()

