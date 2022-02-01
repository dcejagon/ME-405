"""
    @file                    ClosedLoop.py
    @brief                   This file provides the code to interface directly with the encoder hardware
    @author                  Daniel Gonzalez
    @author                  Nolan Clapp
    @author                  Caleb Kephart
    @date                    January 31, 2022
"""
import utime
import time
#from matplotlib import pyplot as plt

class ClosedLoop:
    ''' @brief Puts system into a closed loop.
        @details This code allows us to run the motor/encoder system within a closed loop.
    '''
    
    def __init__(self,Kp,setpoint,EncPosition,duty,time):
        ''' @brief          Constructs a closed loop object
            @details        Sets up the closed loop so that it can intake data from the encoder and main to send to the motor driver.
            @param Kp       This parameter allows us to choose the gain utilized by the system
            @param EncPosition  This parameter allows for the class to intake the encoder position data
            @param duty     This parameter chooses the duty cycle for the motor
            @param time     This parameter sets a timer to be used for the data collection
            
        '''
        ## @brief System Gain
        #
        self.Kp=Kp
        ## @brief Desired encoder position
        #
        self.setpoint=setpoint
        ## @brief Actual Encoder Position
        #  @details Allows for the class to read encoder position data from the 
        #           encoder.
        #
        self.EncPosition=EncPosition
        ## @brief sets duty cycle for motor
        #
        self.duty=duty
        ## @brief sets timer for data collection
        #
        self.time=time
        ## @brief array of time data
        #
        self.Time=[]
        ## @brief array of actual position data
        #
        self.Pos=[]
        ## @brief starting time of data collection 
        #
        self.starttime=time.ticks_ms()
    def Setpoint(self,setpoint):
        self.setpoint=setpoint.read()
        
    def SetKp(self,Kp):
        self.Kp=Kp.read()
        
            
    def control_loop(self):
        ## @brief the error between actual and desired position
        #
        self.error=self.EncPosition.read()-self.setpoint.read()
        ## @brief the duty cycle required for the system to correct with set gain.
        # 
        self.actuation=self.Kp.read()*self.error
        
        self.duty.write(self.actuation)
        
        
        utime.sleep_ms(10)
        #print(time.ticks_ms(),self.EncPosition.read())
        
        self.Time.append(time.ticks_diff(time.ticks_ms(),self.starttime))
        self.Pos.append(self.EncPosition.read())
    # def printdata(self):
        
    #     print(self.Time,self.Pos)
        
    def printdata(self):
        ## @brief index of arrays
        #
        n=0
        while n< len(self.Time):
            print(self.Time[n],self.Pos[n])
            n=n+1
     
        
        
    
    
    
        

