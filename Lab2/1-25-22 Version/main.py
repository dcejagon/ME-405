"""
    @file                    main.py
    @brief                   main file which handles all drivers tasks and shares
    @author                  Daniel Gonzalez
    @author                  Nolan Clapp
    @author                  Caleb Kephart
    @date                    January 31, 2022
"""

import EncoderDriver
import MotorDriver
import ClosedLoop
import shares

import pyb
import time


en_pin=pyb.Pin (pyb.Pin.board.PA10, pyb.Pin.OUT_PP)
in1pin=pyb.Pin (pyb.Pin.board.PB4, pyb.Pin.OUT_PP)
in2pin=pyb.Pin (pyb.Pin.board.PB5, pyb.Pin.OUT_PP)
timer=3
ENCpin1=pyb.Pin (pyb.Pin.board.PB6)
ENCpin2=pyb.Pin (pyb.Pin.board.PB7)
timernumber=4

#4096 ticks is one rotation 
setpoint=shares.Share(4096*4)
EncPosition=shares.Share(0)
Kp=shares.Share(.1)
actuation=shares.Share()
duty=shares.Share(0)

motor1=MotorDriver.MotorDriver(en_pin, in1pin, in2pin, timer,duty)

ENC1=EncoderDriver.EncoderDriver(ENCpin1,ENCpin2,timernumber,EncPosition)
Cl1=ClosedLoop.ClosedLoop(Kp,setpoint,EncPosition,duty,time)



# x = input('Enter 1 to run step: ')

while True:
    try:
        ENC1.read()
        Cl1.control_loop()
        motor1.set_duty_cycle(duty.read())
       
        
    except KeyboardInterrupt:
        Cl1.printdata()
        motor1.set_duty_cycle(0)
        print('Stop Data')
        break
