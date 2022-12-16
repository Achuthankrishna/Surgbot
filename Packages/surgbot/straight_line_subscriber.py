#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist


def callback(msg):
    print("Received velocity command - ", msg.data) 

def main():
    try:
        rospy.init_node('straight_line_subscriber')
        sub = rospy.Subscriber('/surgbot/cmd_vel', Twist, callback, queue_size=10)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

if __name__=="__main__":
    main()