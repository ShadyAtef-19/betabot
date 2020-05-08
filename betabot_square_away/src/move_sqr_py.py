#!/usr/bin/env python

from __future__ import division
import rospy
import math
from geometry_msgs.msg import Twist, Point



rospy.init_node('betabot_square_away')

r=rospy.Rate(10)


publish_msg=rospy.Publisher('cmd_vel' , Twist, queue_size=1)

#defining the length of square side, linear and angular veclocities, and update/refresh rate
side_length=1
linear_velcoity=0.2
angular_velcoity=0.3
update_rate = 10

#calculate the time taken for a given velcity
time_linear=int(side_length/linear_velcoity)
time_angular=int((math.pi/2)*side_length/angular_velcoity)


while True:
    #Publish Twist Message to move the betabot
    twist=Twist()
    for i in range(update_rate* time_linear):
        twist.angular.z=0
        twist.linear.x=linear_velcoity
        publish_msg.publish(twist)
        r.sleep()

    for j in range(update_rate* time_angular):
        twist.linear.x= 0
        twist.angular.z= angular_velcoity
        publish_msg.publish(twist)
        r.sleep()
