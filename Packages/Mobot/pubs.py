#!usr/bin/env python3
import rospy
import math

from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

def vel():
        t= Twist()
        o =Odometry()
        o.header.frame_id = 'odom'
        o.child_frame_id= 'base_link'
        init_xpos = o.pose.pose.position.x
        init_ypos = o.pose.pose.position.y
        print("initial: ",init_xpos, init_ypos)
        rospy.init_node('Robot_pose', anonymous=True)
        pub_twist = rospy.Publisher('/mobot/cmd_vel', Twist, queue_size=10)
        
        rate = rospy.Rate(10) # 10hz
        
        Kp=0.2
        goal_x_pos = 1.0
        goal_y_pos = 1.0
        i=0
        j=0
        y_vel = 1
        x_vel=1
        y1= goal_y_pos-init_ypos
        x1= goal_x_pos-init_xpos
        while(i!=(y1+y_vel)):
            print('\n current iter:', i)
            t.linear.y = y_vel
            pub_twist.publish(t)
            i=i+y_vel
            print("Odometry: values\n", o.pose.pose.position)
            rospy.sleep(1) 
        
        t.linear.y = 0
        pub_twist.publish(t)

        while(j!=(x1)):
            print('\nupdated j:', j)
            t.linear.x = x_vel
            pub_twist.publish(t)
            j=j+x_vel
            rospy.sleep(1)

        t.linear.x=0
        pub_twist.publish(t)

   
if __name__ == '__main__':
       try:
           vel()
       except rospy.ROSInterruptException:
           pass