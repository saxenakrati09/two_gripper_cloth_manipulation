# two_gripper_cloth_manipulation
Blender cloth manipulation

Blender file contains the Blender game engine model where two grippers pull the cloth down.
left_gripper.py and right_gripper.py can be used to save data such as force on the grippers, velocity, time/frames.
Force has been measured using change in momentum. Linear velocity and mass has been used for that.

The data saves to the folder 'forceapplied'. Since the data appends, you need to change the file names 
in above python files everytime you save a new data.

'/forceapplied/cloth_forces_gravity.py' can be used to visulaize the data.

The final visualizations are saved in 'force_applied.png' and 'simple_positionbased.png'
