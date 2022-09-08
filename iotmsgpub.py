#!/usr/bin/env python3

import rospy
from ros_basic_tutorials.msg import iotsensor
import random

def talker():
    pub = rospy.Publisher('iot_sensor_topic', iotsensor, queue_size=10) #creatin the publisher with the name pub and topic name = chatter. string is the type of the msgs
    rospy.init_node('iot_sensor_publisher_node',anonymous=True) #initializing the node
    rate = rospy.Rate(1) #setting the rateof the msgs to publish per second
    i = 0
    while not rospy.is_shutdown(): #keep publishing until the ctrl+c is pressed(rospy is closed)
        iot_sensor = iotsensor() # the msg to publish
        iot_sensor.id = 1
        iot_sensor.name = "slave1"
        iot_sensor.temperature = 37.9 + (random.random()*2)
        iot_sensor.humidity = 90.0 + (random.random()*2)
        rospy.loginfo("I publish")
        rospy.loginfo(iot_sensor)
        pub.publish(iot_sensor)
        rate.sleep()
        i = i+1

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass