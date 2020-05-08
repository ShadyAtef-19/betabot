#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

'''
angle_min = msg.angle_min
angle_max = msg.angle_max
angle_increment = msg.angle_increment
'''

def callback(msg):

    print msg.ranges[999]
    
    move.linear.x = 0.1
    if msg.ranges[999] < 1:
        move.linear.x = 0
        pub.publish(move)
    

'''
    print angle_min
    print angle_max
    print angle_increment
'''

'''
    #print msg.ranges[359]
    
    move.linear.x = 0.1
    if msg.ranges[359] < 1:
        move.linear.x = 0
        pub.publish(move)
    
'''




rospy.init_node('rand_mover2')
sub = rospy.Subscriber("scan", LaserScan, callback)
pub = rospy.Publisher('/cmd_level', Twist)
move = Twist()

rospy.spin()