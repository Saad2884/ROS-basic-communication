#!/usr/bin/env python3

import rospy
from ros_basic_tutorials.msg import iotsensor
import random

def iot_sensor_callback(iot_sensor_message): #getting the caller id: get fully reoslved name of node
    rospy.loginfo("new iot data received:  (%d, %s, %.2f, %.2f,)", # the message
        iot_sensor_message.id, iot_sensor_message.name, iot_sensor_message.temperature, iot_sensor_message.humidity)

def listener():
    rospy.init_node('iot_sensor_subscriber_node', anonymous=True)
    rospy.Subscriber('iot_sensor_topic', iotsensor, iot_sensor_callback) # chatter is the name of topic and String is the type of the msg (should be same for both sub and pub)
    rospy.spin() #keeps python form exiting until this node is stopped

if __name__ == '__main__':
    listener()