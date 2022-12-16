ENPM662 -> Project2

Files: 

 
Mobot - Consists of all main package files : 
to run : teleop_template to run mobile robot and arm_movement to run teleop for manipulator
to run : pub.py for publisher
to run : arm_urdf.launch for the main launch files

to run : python3 invk.py for inverse kinematics and trajectory generation
to run : python3 fwk.py for forward kinematics 

Analaysis1.xml - A Roboanalyser file for all the validation and verification done 

Models:
All important models for environment simulation . Please copy into your .gazebo folder before any simulation

surgbot - consists of all main files for moveit simulation 
Note: This is a copy of Mobot , but only for moveit simulation


Movebot : 
This file consists of all launch files for move it operation including a custom world to simulate 
to run : roslaunch demo_gazebo.launch for simulation

Report : ENPM662- Final Report.pdf

Vidoes : 
Consists of Output videos of the following
a) Video of the robot motion and arm pick and place
b) Arm pick and place using moveit
c) workspace generation manually

CAD Files :
Consists of all the important assembly files along with part files of the manipulator 