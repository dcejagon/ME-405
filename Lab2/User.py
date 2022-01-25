# -*- coding: utf-8 -*-
''' @file                       User.py
    @brief                      A task file for interacting with users
    @details                    This task file interacts with users wanting to take information off of an
                                encoder. This gives instruction to the encoder task which then interacts with
                                the encoder hardware
                                
    @author                     Peyton Archibald
    @author                     Caleb Kephart
    @date                       October 21, 2021
'''
import pyb

class User:
    '''                                                 @brief                  Interface with users
                                                        @details                This class is used to interact with users wanting to take information off
                                                                                encoder hardware
    '''
    def __init__(self, Kp, setpoint):
        
        '''             @brief              Constructs an encoder task object
                        @details            Upon instantiation, the user task object is created with the input parameter
                                                                            of action_Share, which is used to communicate desired actions requested by 
                                                                            the user to the encoder task. 
                        @param action_Share The share used to communicate action requests to the encoder task
                        @param duty_Share   The share used to communicate the duty level requested to the motor task
                        @param gain_Share  The share used to communicate the gain and its changes throughout the tasks.
        '''
        ## @brief   Variable for the action share
        #  @details Initializes the action share and allows for the share to be used within this task.
        #
        self.Kp = Kp
        ## @brief   Variable for the duty share
        #  @details Initializes the duty share and allows for the share to be used within this task.
        #
        self.setpoint = setpoint
        ## @brief   Variable for the USB port
        #  @details Initializes the USB port and allows for the code to transfer information through this port
        #
        self.ser_port = pyb.USB_VCP()
        ##  @brief     collectionState is used to switch collection states.
        #   @details   Allows for the user task to be switched into a collective state where the user inputs values for the duty of motors. 
                                                       #
    
      
        
        print ('Lab2 Testing Interface')
        print ('press n ---- set Kp')
        print ('press i ---- set setpoint')
        
            
        
    def User_input(self):
        '''                                             @brief              Designates shares based on user input.
                                                        @details            After the user has been presented with the prompts, user will input the corresponding character
                                                                            to the desired action. The action share is then modified to be shared to the appropriate task.                                                                              
        '''
        if self.ser_port.any():
            ## @brief    Collects the user input
            #  @details  Once the user is prompted for an input, this variable is changed based off of the input of the user. The shares are then changed based off of the new value of the variable, and program behaves accordingly.
            #
            self.user_in = self.ser_port.read(1)
            
            if self.user_in == b'n':                                        # Sets encoder 1 to zero position
                print('Enter desired gain')
                self.collect = 1
                self.numStr = '' 
            
            elif self.user_in == b'i':                                      # Sets encoder 2 to zero position
                print('Enter desired setpoint')
                self.collect = 2
                self.numStr = ''   
            
        
                
                
            if self.collect > 0:
                ## @brief           Takes in the user input for the duty cycle.
                #  @details         Once the task is switched to collection state, this variable will take in the user character input for the duty cycle.
                #
                self.char_in = self.user_in.decode()
                if self.char_in.isdigit() == True:
                    self.numStr += self.char_in
                    self.ser_port.write(self.char_in)
                if self.char_in == '-' and self.numStr == '':
                    self.numStr += self.char_in
                    self.ser_port.write(self.char_in)
                if self.char_in == '\x7f':
                    self.numStr = self.numStr[:-1]
                    self.ser_port.write(self.char_in)
                if self.char_in == '\r' or self.char_in == '\n':
                    self.number = float(self.numStr)
                    print('\n')
                    if self.collect == 1:
                        self.Kp.write(self.number)
                        self.collect = 0
                        print("Gain set to", self.numStr)
                        self.numStr = '' 
                        
                    elif self.collect == 2:
                        self.setpoint.write(self.number)
                        print("setpoint set to", self.numStr, '\n')
                        self.numStr = '' 
                        
                        
                    

                
                