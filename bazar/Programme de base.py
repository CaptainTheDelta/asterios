# coding: utf8

from gopigo import*
import numpy as np
from time import sleep # permet de faire une pause de X secondes
from time import time  # permet de connaitre le temps écoulé depuis Epoch en seconde

#######################
# Gestion des moteurs #
#######################

#Move the GoPiGo forward
# fwd()

#Move GoPiGo back
# bwd()

#Turn GoPiGo Left slow (one motor off, better control)	
# left():
#Rotate GoPiGo left in same position (both motors moving in the opposite direction)
# left_rot()

#Turn GoPiGo right slow (one motor off, better control)
# right():
#Rotate GoPiGo right in same position both motors moving in the opposite direction)
# right_rot():

#Stop the GoPiGo
# stop():

########################
# Vitesses des moteurs #
########################

#Set speed of the left motor
#	arg: speed-> 0-255
# set_left_speed(speed):
	
#Set speed of the right motor
#	arg: speed-> 0-255
# set_right_speed(speed):

#Set speed of the both motors
#	arg: speed-> 0-255
# set_speed(speed):

#Increase the speed
# increase_speed():
#Decrease the speed
# decrease_speed():

#read_motor_speed()

#################
# Roues codeuse #
#################

#Set encoder targeting on
#arg:   m1: 0 to disable targeting for m1, 1 to enable it
#	m2:	1 to disable targeting for m2, 1 to enable it
#	target: number of encoder pulses to target (18 per revolution)
# enc_tgt(m1,m2,target):

#Read encoder value
#	arg:  motor -> 	0 for motor1 and 1 for motor2
#	return:		distance in cm
# enc_read(motor):

#####################
# Ultrason et servo #
#####################

#Read ultrasonic sensor
#	arg: pin -> 	Pin number on which the US sensor is connected 
#	return:		distance in cm
# us_dist(pin):


#Set servo position
#	arg:
#		position: angle in degrees to set the servo at
# servo(position):

#Enables the servo
# enable_servo():

#Disable the servo
# disable_servo():

##########
# Divers #
##########

#Read voltage
#	return:	voltage in V
# volt():

#Trim test with the value specified
# trim_test(value):
    
#Read the trim value in	EEPROM if present else return -3
# trim_read():

#Write the trim value to EEPROM, where -100=0 and 100=200
# trim_write(value):

if __name__ == "__main__":
    stop()
    fwd()
    servo(45)
    sleep(.5)
    servo(135)
    sleep(.5)
    servo(90)
    sleep(.5)
    disable_servo()
    stop()


