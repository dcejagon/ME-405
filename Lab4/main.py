# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 08:28:34 2022

@author: nclap
"""
import task_share
import pyb
import micropython
from pyb import ADC
import time

micropython.alloc_emergency_exception_buf(100)


q0 = task_share.Queue ('L', 1000, thread_protect = False, overwrite = False, name = "Queue 0")



pinC1=pyb.Pin(pyb.Pin.cpu.C1, pyb.Pin.OUT_PP)
pinC0=pyb.Pin(pyb.Pin.cpu.C0)
myadc=pyb.ADC(pinC0)
pinC1.low()
time.sleep(1)
tim1=pyb.Timer(1)
tim1.init(freq=100)

def interruptfunc(tim1):
    
    q0.put(myadc.read(),in_ISR=True)
    #print("interrupt")
    
#tim1.callback(interruptfunc)
#q0.put(myadc.read())

x=int(input())
tim1.callback(interruptfunc)
pinC1.high()
while x<=10:
    try: 
        print(q0.get())
        time.sleep_ms(5)
    except KeyboardInterrupt: 
        print("Stop Data")
        tim1.callback(None)
