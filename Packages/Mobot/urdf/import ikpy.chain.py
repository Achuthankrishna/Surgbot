import ikpy.chain
import numpy as np


def deg2rad(th):
    return th * np.pi / 180


my_chain = ikpy.chain.Chain.from_urdf_file("Mobot.urdf")
th1 = float(input("Enter rotation (in deg) for link_2: "))
th2 = float(input("Enter rotation (in deg) for link_3 "))
th3 = float(input("Enter rotation (in deg) for link_4: "))
th4 = float(input("Enter rotation (in deg) for link_5: "))
th5 = float(input("Enter rotation (in deg) for link_6: "))
th6 = float(input("Enter rotation (in deg) for link_7: "))

target_angle = [0, deg2rad(th1), deg2rad(th2), deg2rad(th3), deg2rad(th4), deg2rad(th5),deg2rad(th6)]
position = my_chain.forward_kinematics(target_angle)

print("Input joint angles: (%s, %s, %s, %s, %s, %s)" % (target_angle[0],
                                                        target_angle[1],
                                                        target_angle[2],
                                                        target_angle[3],
                                                        target_angle[4],
                                                        target_angle[5],
                                                        target_angle[6]))
print("X coordinate for end effector: ", position[0, 3])
print("Y coordinate for end effector: ", position[1, 3])
print("Z coordinate for end effector: ", position[2, 3])
