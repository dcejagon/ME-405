import EncoderDriver
import MotorDriver

import pyb
import time


en_pin=pyb.Pin (pyb.Pin.board.PA10, pyb.Pin.OUT_PP)
in1pin=pyb.Pin (pyb.Pin.board.PB4, pyb.Pin.OUT_PP)
in2pin=pyb.Pin (pyb.Pin.board.PB5, pyb.Pin.OUT_PP)
timer=3
motor1=MotorDriver.MotorDriver(en_pin, in1pin, in2pin, timer)
motor1.set_duty_cycle(50)


ENCpin1=pyb.Pin (pyb.Pin.board.PB6)
ENCpin2=pyb.Pin (pyb.Pin.board.PB7)
timernumber=4
ENC1=EncoderDriver.EncoderDriver(ENCpin1,ENCpin2,timernumber)
while True:
    try:
        
        ENC1.read()
        time.sleep(.25)
    except KeyboardInterrupt:
        motor1.set_duty_cycle(0)
        break
