# Motor/Encoder Test CODE
import time
'''
pinA10 = pyb.Pin (pyb.Pin.board.PA10, pyb.Pin.OUT_PP)
pinB4 = pyb.Pin (pyb.Pin.board.PB4, pyb.Pin.OUT_PP)
pinB5 = pyb.Pin (pyb.Pin.board.PB5, pyb.Pin.OUT_PP)
tim3 = pyb.Timer (3, freq=20000)
ch1 = tim3.channel (1, pyb.Timer.PWM, pin=pinB4)
ch2 = tim3.channel (2, pyb.Timer.PWM, pin=pinB5)

pinA10.high()
pinB4.low()

ch1.pulse_width_percent(0)
ch2.pulse_width_percent(0)
'''

pinB6 = pyb.Pin (pyb.Pin.board.PB6)
pinB7 = pyb.Pin (pyb.Pin.board.PB7)

tim4 = pyb.Timer(4, prescaler=0, period=65535)
    
ENCch1= tim4.channel(1, pyb.Timer.ENC_AB, pin=pinB6)
ENCch2= tim4.channel(2, pyb.Timer.ENC_AB, pin=pinB7)
while True:
    try:
        print(tim4.counter())
        time.sleep(.5)
    except:
        pass

"""
count=tim8.counter()
delta=count-countprev

#check delta and fix
if delta>period/2:
    delta-=period

elif delta< -period/2:
    delta+=period


#add delta to position variable to 
EncoderPos+=self.delta
#make previous count = current count 
countprev=count

print(EncoderPos)
"""