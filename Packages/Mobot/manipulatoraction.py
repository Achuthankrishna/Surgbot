from sympy import * 
import rospy
from std_msgs.msg import Float64
from sympy.matrices import Matrix
from sympy import pprint
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def talker():
    pub_joint_1 = rospy.Publisher('mobot/link_1_motor/command', Float64, queue_size=10)
    pub_joint_2 = rospy.Publisher('mobot/link_2_motor/command', Float64, queue_size=10)
    pub_joint_3 = rospy.Publisher('mobot/link_3_motor/command', Float64, queue_size=10)
    pub_joint_4 = rospy.Publisher('mobot/link_4_motor/command', Float64, queue_size=10)
    pub_joint_5 = rospy.Publisher('mobot/link_5_motor/command', Float64, queue_size=10)
    pub_joint_6 = rospy.Publisher('mobot/link_6_motor/command', Float64, queue_size=10)
    pub_ee=rospy.Publisher('mobot/link_7_motor/command', Float64, queue_size=10)
    pub_ee1=rospy.Publisher('mobot/link_8_motor/command', Float64, queue_size=10)

    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(100)
    pub_joint_1.publish(0)
    pub_joint_2.publish(0)
    pub_joint_3.publish(0)
    pub_joint_4.publish(0)
    pub_joint_5.publish(0)
    pub_joint_6.publish(0)
    pub_ee.publish(0)
    pub_ee1.publish(0)
    rospy.sleep(5)
    pub_joint_2.publish(1.5)
    pub_joint_3.publish(-1.5)
    pub_ee.publish(-0.03)
    pub_ee1.publish(0.03)
    rospy.sleep(10)
    pub_ee.publish(-0.00)
    pub_ee1.publish(0.00)
    rospy.sleep(5)
    pub_joint_2.publish(-0.5)
    pub_joint_3.publish(-1.0)

talker()