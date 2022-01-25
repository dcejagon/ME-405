
class ClosedLoop:
    
    def __init__(self,Kp,setpoint,EncPosition,duty):
        self.Kp=Kp
        self.setpoint=setpoint
        self.EncPosition=EncPosition
        self.duty=duty
        
    def Setpoint(self,setpoint):
        self.setpoint=setpoint.read()
        
    def SetKp(self,Kp):
        self.Kp=Kp.read()
        
            
    def control_loop(self):
        self.error=self.EncPosition.read()-self.setpoint.read()
        
        self.actuation=self.Kp.read()*self.error
        self.duty.write(self.actuation)
        #print(self.duty.read())
    
    
    
        

