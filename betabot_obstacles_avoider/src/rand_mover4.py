#!/usr/bin/env python

import rospy
import math
import sys, select, termios, tty

from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32

range_front = Float32()
range_left = Float32()
range_right = Float32()
range_left_front = Float32()
range_right_front = Float32()

normal_vel =0.2 #linear velocity without obstacles 
normal_angul =1.5 #angular velocity without obstacles 
ob_vel =0 #linear velocity with obstacles
ob_angul = 0.2 #angular velocity with obstacles
rays_count = 100 #number of laser rays to consider


def callback(data):
	
	#defining directions for the robot
	rospy.loginfo("ranges %f", data.ranges[1499])
	range_front.data= data.ranges[1499]
	range_left.data= data.ranges[0]
	range_right.data= data.ranges[999]
	range_left_front.data= data.ranges[1749]
	range_right_front.data= data.ranges[1249]


'''	rospy.loginfo("ranges %f", data.ranges[1499])
	range_front.data= min(data.ranges[1499-rays_count: 1499+rays_count])
	range_left.data= min(data.ranges[100-rays_count: 100+rays_count])
	range_right.data= min(data.ranges[999-rays_count: 999+rays_count])
	range_left_front.data= min(data.ranges[1749-rays_count: 1749+rays_count])
	range_right_front.data= min(data.ranges[1249-rays_count: 1249+rays_count])
'''



def move():
    
    pub = rospy.Publisher('cmd_vel', Twist)
    sub = rospy.Subscriber("scan", LaserScan, callback)
    rospy.init_node('rand_mov', anonymous=True)
    rate = rospy.Rate(10) # 10Hz
    twist = Twist()
    while not rospy.is_shutdown():
		# The front space is empty of obstacles
		if (range_front.data>1):
			twist.linear.x =normal_vel; twist.linear.y = 0; twist.linear.z = 0
		        twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
		        pub.publish(twist)
			#There is an obstacle on the front left
			if (range_left_front.data<0.2):
				twist.linear.x = ob_vel; twist.linear.y = 0; twist.linear.z = 0
				twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = ob_angul
				pub.publish(twist)
			#There is an obstacle on the front right
			elif (range_right_front.data<0.2):
				twist.linear.x = ob_vel; twist.linear.y = 0; twist.linear.z = 0
				twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = -ob_angul
				pub.publish(twist)
		    	
		# The front space has obstacles
		else :
			#Left or front left spaces are clear
			if (range_left_front.data>1) or (range_left.data>1):
				twist.linear.x = ob_vel; twist.linear.y = 0; twist.linear.z = 0
				twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = -normal_angul
				pub.publish(twist)
			
			#Right or front right spaces are clear
			elif (range_right_front.data>1) or (range_right.data>1) :
				twist.linear.x = ob_vel; twist.linear.y = 0; twist.linear.z = 0
				twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = normal_angul
				pub.publish(twist)
			
			#Space on the left is greater than space on the right
		    	elif (range_left.data>range_right.data):
			    	twist.linear.x = ob_vel; twist.linear.y = 0; twist.linear.z = 0
			    	twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = -normal_angul
			    	pub.publish(twist)
			    
		    	else :
                            twist.linear.x =ob_vel; twist.linear.y = 0; twist.linear.z = 0
                            twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = normal_angul
                            pub.publish(twist)

			   
                   
 		rate.sleep()

if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException:
        pass


