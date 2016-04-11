#!/usr/bin/env python

import rospy
from race.msg import drive_values
from race.msg import drive_param
from std_msgs.msg import Bool

"""
What you should do:
 1. Subscribe to the keyboard messages (If you use the default keyboard.py, you must subcribe to "drive_paramters" which is publishing messages of "drive_param")
 2. Map the incoming values to the needed PWM values
 3. Publish the calculated PWM values on topic "drive_pwm" using custom message drive_values
"""

def talk(data):
  pub = rospy.Publisher('drive_pwn', drive_values, queue_size=10)
  print "Recieved Velocity: ", data.velocity
  print "Recieved Angle: ", data.angle
  msg = drive_values()
  msg.pwm_drive = (data.velocity + 100)*3277/100 + 6554
  msg.pwm_angle = (data.angle + 100)*3277/100 + 6554
  pub.publish(msg)

rospy.init_node('talker', anonymous=True)
sub = rospy.Subscriber('drive_parameters', drive_param, talk)
rospy.spin()
