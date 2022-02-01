# Control System Description and Results
## Description
### Overall 
Our control system uses just position control at the moment. We plan to add 
integral control eventually to eleminate steady state error from our system. 
Right now, we are able to specify a desired position, and supply the motor
with the correct duty cycle based on the current encoder readings. The farther
away from the set point that we are, the higher duty cycle we apply to
the motor. Similarly, as we approach the set point, our supplied duty gets 
smaller and smaller. This allows us to stop the wheel from rotating when
it reaches the declared set point. 
### Physical Implementation
This is position control is acomplished by subtracting the encoder position 
from the set point and then multiplying it by our Kp value. This produces what 
is known as an 'Actuation Signal' which we will feed back into our motor driver
to act as the duty we want to set. 
### Choosing the correct Kp
Choosing the correct proportional gain is crucial to get the desired system 
response. We began by selecting an arbitrary gain value to start and analyzing
the system response. If the system oscillated heavily, Kp is too high, but if 
it does not respond enough (or at all) Kp is too low. The response from this 
tuning is seen in the 'Results' section below. 
## Tuning Results
### Initial Arbitrary Kp Value
The plot below shows the system response to our first Kp input. We were then
able to analyze the response and choose a more suitable Kp value. 
![System Response to initial Kp=INSERT FIRST KP HERE](INSERT_IMAGE_HYPERLINK_HERE)
System Response to initial Kp=INSERT FIRST KP HERE]
### Next Kp
The plot below shows our system response to a tuned Kp. 
![System Response to Kp=INSERT FIRST KP HERE](INSERT_IMAGE_HYPERLINK_HERE)
System Response to Kp=INSERT FIRST KP HERE]
### Tuned Kp
The plot below shows our system response to a Kp value that we found suitable 
for our system. 
![System Response to Kp=INSERT FIRST KP HERE](INSERT_IMAGE_HYPERLINK_HERE)
System Response to Kp=INSERT FIRST KP HERE]