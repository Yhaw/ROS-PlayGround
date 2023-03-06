# ROS-PlayGround

1. Create Workspace...
2. Pull pull repo, copy src into workspace
3. catkin_make

To control the rover open another terminal and type this

rosrun teleop_twist_keyboard teleop_twist_keyboard.py cmd_vel:=/mobile_base_controller/cmd_vel
