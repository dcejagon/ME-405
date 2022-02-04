# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 17:21:48 2022

@author: dceja
"""

import matplotlib.pyplot as plt
import random

def flusim():
    state = 0 
    
    while True:
        # Flu Chance
        x = random.uniform(0,100)
        # Vaccine Chance
        v = random.uniform(0,100)
        # No Flu    
        if state == 0:
            if x >= 50 or v < 10: 
                state = 1
            elif x < 50 and v >=10:
                state = 0
        # Mild Flu
        elif state == 1:
           if x >= 50 and v >= 10:
               state = 2
           elif x < 50 and v >= 10:
               state = 0
           elif v < 10: 
               state = 3       
        # Severe Flu
        elif state == 2:
           if x < 50: 
               state = 1
           elif x >= 50:
      
              state = 2
        yield state
        
def plot(day, state):
    
    
    plt.plot(day, state)
    plt.plot(day, state, 'or')
    
    # Axis Labeling
    plt.xlabel('Day #') 
    plt.yticks([0,1,2,3], labels = ['No Flu','Mild Flu','Severe Flu','Recovered']) 
        
    # Graph Title
    plt.title('50-Day Flu Season') 
    
    plt.show()
                
if __name__ == "__main__":
    
    day = 0
    x_list = []
    y_list = []
    flu = flusim()
    
    while day < 50:
       day = day + 1 
       x_list.append(day)
       y_list.append(next(flu))
     
plot(x_list, y_list) 