import utime
import time
#from matplotlib import pyplot as plt

class ClosedLoop:
    
    def __init__(self,Kp,setpoint,EncPosition,duty,time):
        self.Kp=Kp
        self.setpoint=setpoint
        self.EncPosition=EncPosition
        self.duty=duty
        self.time=time
        self.Time=[]
        self.Pos=[]
        self.starttime=time.ticks_ms()
    def Setpoint(self,setpoint):
        self.setpoint=setpoint.read()
        
    def SetKp(self,Kp):
        self.Kp=Kp.read()
        
            
    def control_loop(self):
        self.error=self.EncPosition.read()-self.setpoint.read()
        self.actuation=self.Kp.read()*self.error
        
        self.duty.write(self.actuation)
        
        
        utime.sleep_ms(10)
        #print(time.ticks_ms(),self.EncPosition.read())
        
        self.Time.append(time.ticks_diff(time.ticks_ms(),self.starttime))
        self.Pos.append(self.EncPosition.read())
    # def printdata(self):
        
    #     print(self.Time,self.Pos)
        
    def printdata(self):
        n=0
        while True:
            try:
                if n<=len(self.Time) or n<=len(self.Pos):
                    print(self.Time[n],self.Pos[n])
                    n+=1
                else:
                    pass
                
            except KeyboardInterrupt:
                break
    
        
        
    
    
    
        

