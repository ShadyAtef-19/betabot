#!/usr/bin/env python

import rospy
import math

from geometry_msgs.msg import Twist 
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32

# import sys, select, termios, tty


class Mover():

	def __init__(self):


		self.pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
		self.sub = rospy.Subscriber("scan", LaserScan, self.callback)

		# definiing the fields to be filled by the laser scanner
		self.range_center = Float32()
		self.range_left = Float32()
		self.range_right = Float32()
		self.range_front_left = Float32()
		self.range_front_right = Float32()


		
		self.max_range= Float32()		# the max readble range for the bot in meteres
		self.min_range= Float32()		# the minimum available range in meteres
		self.angle_min= Float32()        # start angle of the scan [rad]
		self.angle_max= Float32()        # end angle of the scan [rad]
		self.angle_increment= Float32()  # angular distance between measurements [rad]

		self.max_range=8.000000	# the max readble range for the bot in meteres
		self.min_range=0.100000		# the minimum available range in meteres
		self.angle_min=0.000000        # start angle of the scan [rad]
		self.angle_max=6.283120        # end angle of the scan [rad]
		self.angle_increment=0.003143  # angular distance between measurements [rad]




		self.normal_vel =0.35 # the linear velocity applied in normal conditions
		self.normal_angel_turn =2  # the angular velocity applied in normal conditions
		self.last_ob_vel =0 # the velocity applied in case of the existance of a nearby object
		self.last_ob_angel =1.5 # the angular velocity applied in case of  a nearby object
		# half_angel =1.57284 # the half of the angel fo
		self.move()
	def angleToIndex(self,angle):
		angle=angle*math.pi/180
		return -1+(angle-self.angle_min)//self.angle_increment

	def callback(self,data):
		# uncomment if you want to know the data of the current used sensor
		# rospy.loginfo(20*"- ") # 
		# rospy.loginfo("min_angle %f", data.angle_min) 
		# rospy.loginfo("max_angle %f", data.angle_max) 
		# rospy.loginfo("angle increment %f", data.angle_increment) 
		# rospy.loginfo("min range %f", data.range_min) 
		# rospy.loginfo("max range %f", data.range_max) 
		# rospy.loginfo("range length %f", len(data.ranges)) 
		# rospy.loginfo(20*"- ") # range value in front of the bot

		# rospy.loginfo(self.angleToIndex(180)) # range value in front of the bot

		rospy.loginfo("front %f", data.ranges[1499]) # range value in front of the bot

		self.range_left.data= data.ranges[0] # range value on the left of left of the bot
		self.range_front_left.data= data.ranges[1749] # range valuee on the front left of the bot
		self.range_center.data= data.ranges[1499] # range value in front of the bot
		self.range_front_right.data= data.ranges[1249] # range valuee on the front right bot
		self.range_right.data= data.ranges[999] # range value on the right of the bot
		
		#those three can be used to know the exact index of the specific angle we want (for now i have used the numbers i found and applied it)
		self.angle_min=data.angle_min
		self.angle_max=data.angle_max
		self.angle_increment= data.angle_increment

	def move(self):
		
		rospy.init_node('mazer', anonymous=True)
		rate = rospy.Rate(10) # 10hz
		twist = Twist()
		while not rospy.is_shutdown():
		
			if (self.range_center.data>1):# if you still have distance in front of you 

				twist.linear.x =self.normal_vel;# move forward with normal speed
				twist.linear.y = 0;
				twist.linear.z = 0
				twist.angular.x = 0; 
				twist.angular.y = 0; 
				twist.angular.z = 0
				self.pub.publish(twist)
				
				if (self.range_front_left.data<0.2):# if you face an object to your atmost left
					twist.linear.x = self.last_ob_vel;
					twist.linear.y = 0; 
					twist.linear.z = 0
					twist.angular.x = 0; 
					twist.angular.y = 0; 
					twist.angular.z = self.last_ob_angel
					self.pub.publish(twist)

				elif (self.range_front_right.data<0.2):# if you face an object to your atmost right
					twist.linear.x = self.last_ob_vel;
					twist.linear.y = 0;
					twist.linear.z = 0
					twist.angular.x = 0;
					twist.angular.y = 0;
					twist.angular.z = -self.last_ob_angel
					self.pub.publish(twist)

			else :# if you don't have enough distance in front of you
				if (self.range_front_left.data>1) or (self.range_left.data>1):# if the space at your left is free then rotate until your center is open again
					twist.linear.x = self.last_ob_vel;
					twist.linear.y = 0;
					twist.linear.z = 0
					twist.angular.x = 0;
					twist.angular.y = 0;
					twist.angular.z = -self.normal_angel_turn
					self.pub.publish(twist)


				elif (self.range_front_right.data>1) or (self.range_right.data>1) :# if the space at your right is free then rotate until your center is open again
					twist.linear.x = self.last_ob_vel;
					twist.linear.y = 0;
					twist.linear.z = 0
					twist.angular.x = 0;
					twist.angular.y = 0; 
					twist.angular.z = self.normal_angel_turn
					self.pub.publish(twist)

					# if both left and right are smaller than 1 meter then you will have to see which one is wider so that you can move to 

				elif (self.range_left.data>self.range_right.data):# if left is bigger than right
					twist.linear.x = self.last_ob_vel; 
					twist.linear.y = 0; 
					twist.linear.z = 0
					twist.angular.x = 0; 
					twist.angular.y = 0; 
					twist.angular.z = -self.normal_angel_turn
					self.pub.publish(twist)
				
				else : # if right is bigger than left
					twist.linear.x =self.last_ob_vel; 
					twist.linear.y = 0; 
					twist.linear.z = 0
					twist.angular.x = 0; 
					twist.angular.y = 0; 
					twist.angular.z = self.normal_angel_turn
					self.pub.publish(twist)


					#we can add another condition (law elrobot mazno2) but it I will need to know the exact dimensions of the robot
			rate.sleep()
		
if __name__ == '__main__':
	
	try:
		Mover()
		
	except rospy.ROSInterruptException:
		pass
	

