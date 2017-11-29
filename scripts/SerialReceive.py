#!/usr/bin/python

import rospy
import serial
from std_msgs.msg import String

ser = serial.Serial(port = '/dev/ttyACM0', baudrate=115200)

def SerialReceive():
	pub = rospy.Publisher("sr", String, queue_size=10)

	rospy.init_node('SerialReceive', anonymous=True)

	rate = rospy.Rate(10)

	rospy.loginfo("Serial Receiving Start")

	while not rospy.is_shutdown():
		tmp = ser.readline()

		pub.publish(tmp)

if __name__ == '__main__':
	try:
		SerialReceive()
	except rospy.ROSInterruptException:
		pass
