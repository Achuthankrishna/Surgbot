#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

def callbackj1(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard j1 %f", data.data)
def callbackj2(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard j2 %f", data.data)
def callbackj3(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard j3 %f", data.data)
def callbackj4(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard j4 %f", data.data)
def callbackj6(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard j6 %f", data.data)
def callbackj7(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard j7 %f", data.data)
def callbackj8(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard j8 %f", data.data)
def callbackhj11(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard hj11 %f", data.data)
def callbackhj12(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard hj12 %f", data.data)
def callbackhj21(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard hj21 %f", data.data)
def callbackhj22(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard hj22 %f", data.data)
def callbackhj23(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard hj23 %f", data.data)
def callbackhj31(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard hj31 %f", data.data)
def callbackhj32(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard hj32 %f", data.data)
def callbackhj33(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard hj33 %f", data.data)    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("Mobot/link_1_motor/command", Float64, callbackj1)
    rospy.Subscriber("Mobot/link_2_motor/command", Float64, callbackj2)
    rospy.Subscriber("Mobot/link_3_motor/command", Float64, callbackj3)
    rospy.Subscriber("Mobot/link_4_motor/command", Float64, callbackj4)
    rospy.Subscriber("Mobot/link_5_motor/command", Float64, callbackj6)
    rospy.Subscriber("Mobot/link_6_motor/command", Float64, callbackj7)
    rospy.Subscriber("Mobot/link_7_motor/command", Float64, callbackhj11)
    rospy.Subscriber("Mobot/link_8_motor/command", Float64, callbackhj12)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()