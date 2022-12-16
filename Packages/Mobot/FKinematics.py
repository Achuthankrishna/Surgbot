from sympy import *
init_printing()
l1,l2,l3 = symbols('l_1 l_2 l_3')
x,y,z=symbols("x y z")
d1,d2,d3=symbols("d1 d2 d3")
alpha=symbols("alpha")
#alpha is the angle between the prvious joint's z-axis and current joint's z-axis about the common normal(x-axis).
theta1,theta2,theta3,theta4,theta5,theta6,theta7= symbols('theta1 theta2 theta3 theta4 theta5 theta6 theta7')


def DHP(alpha,a,dz,angle,i):
    #The common DH representation is given as follows
    TM = Matrix([[cos(angle),-sin(angle)*cos(alpha),sin(angle)*sin(alpha),a*cos(angle)],
                    [sin(angle),cos(angle)*cos(alpha),-cos(angle)*sin(alpha),a*sin(angle)],
                    [0,sin(alpha),cos(alpha),dz],
                    [0,0,0,1]])
    print("The transformation matrix",i ,"/n")
    pprint(TM)
    return TM

d1= 342.96
d4= 410.45
d6= 127
a1= 69.55
a2= 350.5
a3= 47.38
a6= 0

theta1=theta2=theta3=theta4=theta5=theta6=theta7=0
#STEP 1: find overall transition matrix
Tr1=DHP(pi/2,a1,d1,theta1,1)
Tr2=DHP(0,a2,0,pi/2 +theta2,2)
Tr3=DHP(pi/2,a3,0,theta3,3)
Tr4=DHP(-pi/2,0,d4,theta4,4)
Tr5=DHP(pi/2,0,0,-pi/2 +theta5,5)
Tr6=DHP(0,a6,d6,theta6,6)

Tendffector = Tr1*Tr2*Tr3*Tr4*Tr5*Tr6
print("transformation matrix for operation 1:")
pprint(Tendffector)

