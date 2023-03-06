# ROS-PlayGround

1. Create Workspace...
2. Pull pull repo, copy src into workspace
3. catkin_make

To control the rover open another terminal and type this

rosrun teleop_twist_keyboard teleop_twist_keyboard.py cmd_vel:=/mobile_base_controller/cmd_vel


#Install these before proceeding

\\Change noetic to your prefered distro\\

sudo apt-get install ros-noetic-ros-control ros-noetic-joint-state-controller ros-noetic-effort-controllers ros-noetic-position-controllers ros-noetic-velocity-controllers ros-noetic-ros-controllers ros-noetic-gazebo-ros ros-noetic-gazebo-ros-control -y

pip install teleop_twist_keyboard