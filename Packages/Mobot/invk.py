from sympy import * 
import rospy
from std_msgs.msg import Float64
from sympy.matrices import Matrix
from sympy import pprint
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def talker(q):
    pub_joint_1 = rospy.Publisher('mobot/link_1_motor/command', Float64, queue_size=10)
    pub_joint_2 = rospy.Publisher('mobot/link_2_motor/command', Float64, queue_size=10)
    pub_joint_3 = rospy.Publisher('mobot/link_3_motor/command', Float64, queue_size=10)
    pub_joint_4 = rospy.Publisher('mobot/link_4_motor/command', Float64, queue_size=10)
    pub_joint_5 = rospy.Publisher('mobot/link_5_motor/command', Float64, queue_size=10)
    pub_joint_6 = rospy.Publisher('mobot/link_6_motor/command', Float64, queue_size=10)
    
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(100)
    pub_joint_1.publish(q[1])
    pub_joint_2.publish(q[6])
    pub_joint_3.publish(q[2])
    pub_joint_4.publish(q[3])
    pub_joint_5.publish(-q[4])
    pub_joint_6.publish(-q[5])
    #rospy.sleep(1)
    
def Tmatrix(angle,a,dz,alpha,i):
    Trans = Matrix([[cos(angle),-sin(angle)*cos(alpha),sin(angle)*sin(alpha),a*cos(angle)],
                    [sin(angle),cos(angle)*cos(alpha),-cos(angle)*sin(alpha),a*sin(angle)],
                    [0,sin(alpha),cos(alpha),dz],
                    [0,0,0,1]])
    return Trans

d1 = 0.3429 
d4 = 0.4104
d6 = 0.127
a1 = 0.069 #end effector length plus the length of pen
a2=0.350
a3=0.047
a6=0
#Initializing thetas
t_1=Symbol('theta1')
t_2=Symbol('theta2')
t_3=Symbol('theta4')
t_4=Symbol('theta5')
t_5=Symbol('theta6')
t_6 = Symbol('theta7')
t_7= Symbol('theta3')

T1=Tmatrix(t_1,a1,d1,pi/2,1)
T2=Tmatrix(t_2,a2,0,-pi/2,2)
T3=Tmatrix(t_7,a3,0,-pi/2,3)
T4=Tmatrix(t_3,0,d4,pi/2,4)
T5=Tmatrix(t_4,0,0,pi/2,5)
T6=Tmatrix(t_5,a6,d6,-pi/2,6)
T7=Tmatrix(t_6,0,0,0,7)

H1 = T1*T2
H2 = H1*T3
H3 = H2*T4
H4 = H3*T5
H5 = H4*T6
H6 = H5*T7
#Jacobian Calculation
z0= Matrix([0,0,1])
z1= Matrix([H1[0:3,2]])
z2= Matrix([H2[0:3,2]])
z4= Matrix([H3[0:3,2]])
z5= Matrix([H4[0:3,2]])
z6= Matrix([H5[0:3,2]])
z7= Matrix([H6[0:3,2]])

J = Matrix([ [diff(H6[3], t_1), diff(H6[3], t_2), diff(H6[3], t_3), diff(H6[3], t_4), diff(H6[3], t_5), diff(H6[3], t_6)], 
            [diff(H6[7], t_1), diff(H6[7], t_2), diff(H6[7], t_3), diff(H6[7], t_4), diff(H6[7], t_5), diff(H6[7], t_6)], 
            [diff(H6[11], t_1), diff(H6[11], t_2), diff(H6[11], t_3), diff(H6[11], t_4), diff(H6[11], t_5), diff(H6[11], t_6)], 
            [z1, z2, z4, z5, z6, z7]])

print("The Jacobian Matrix")
pprint(J)

#Initial Joint angles
q=[0,0,-pi/2,0,-pi/2,0,0] #sample values for pickup motion
step=10
theta =[i for i in range(0,180,step)] #Already when end efector is at 90, we start from 90 as our starting point and compute
dt = 5/len(theta)   #dt = T/N where T is 5 secs and No.of intervals is len of theta
x = []
y = []
z = []
fig = plt.figure(figsize=(4,4))
ax = fig.add_subplot(111, projection='3d')

for t in theta:
    X_dot = Matrix([[0], [-0.1*(pi/5)*sin(t*(pi/180))], [0.1*(pi/5)*cos(t*(pi/180))], [0], [0], [0]]) # Cartesian velocity matrix of end effector
    Jacobi = J.subs({t_1 : q[0], t_2 : q[1], t_3 : q[2], t_4 : q[3], t_5 : q[4], t_6 : q[5],t_7 : q[6]}) 
    Homog = H6.subs({t_1 : q[0], t_2 : q[1], t_3 : q[2], t_4 : q[3], t_5 : q[4], t_6 : q[5],t_7: q[6]})
    x.append(Homog[3])   # X-component of end effector position
    y.append(Homog[7])   # Y-component of end effector position
    z.append(Homog[11])  # Z-component of end effector position
    print(x)
    print(y)
    print(z)
    ax.scatter3D(y,z,0,'z',20,'Blue',True)
    #plt.scatter(z,y)
    plt.xlim(0, 1)
    plt.ylim(-0.2, 0.2)
    ax.set_xlabel('X-axis', fontweight ='bold')
    ax.set_ylabel('Y-axis', fontweight ='bold')
    ax.set_zlabel('Z-axis', fontweight ='bold')
    q_dot = (Jacobi.pinv()*X_dot).evalf()
    pprint(q)  
    # Obtaining the joint angular velocities Matrix
    for i in range(len(q_dot)):
      q[i]+=(q_dot[i]*dt)
    talker(q)
    pprint(q)  

plt.show()