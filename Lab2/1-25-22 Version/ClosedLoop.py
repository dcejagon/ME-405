"""
    @file                    ClosedLoop.py
    @brief                   This file controls the output speed of the motor
    
    @author                  Daniel Gonzalez
    @author                  Nolan Clapp
    @author                  Caleb Kephart
    @date                    January 31, 2022
"""
class ClosedLoop:
    
    '''@brief       Creates a class for closed loop control on the motor speed
       @details     P-controller drives the measured value to the Setpoint  
    '''
    
    def __init__(self,Kp,setpoint,EncPosition,duty):
        self.Kp=Kp
        self.setpoint=setpoint
        self.EncPosition=EncPosition
        self.duty=duty
        
    def Setpoint(self,setpoint):
        self.setpoint=setpoint.read()
        
    def SetKp(self,Kp):
        
        '''@brief   sets the Kp value
        '''
        
        self.Kp=Kp.read()
            
    def control_loop(self):
        self.error=self.EncPosition.read()-self.setpoint.read()
        
        self.actuation=self.Kp.read()*self.error
        self.duty.write(self.actuation)
        
    
    
    
        

