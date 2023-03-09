#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import sys, select, termios, tty

# Define global variables
speed = 0.2
turn = 0.5

# Define function to get key input from user
def getKey():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

# Define function to publish velocity commands on cmd_vel topic
def moveRobot():
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rospy.init_node('robot_teleop', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    # Initialize Twist message
    vel_msg = Twist()
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    # Continuously get key input and publish velocity commands
    while not rospy.is_shutdown():
        key = getKey()

        if key == 'w':
            vel_msg.linear.x = speed
            vel_msg.angular.z = 0
            print("Forward we go")
        elif key == 's':
            vel_msg.linear.x = -speed
            vel_msg.angular.z = 0
            print("Stop I say")
        elif key == 'a':
            vel_msg.linear.x = 0
            vel_msg.angular.z = turn
            print("Left we go")
        elif key == 'd':
            vel_msg.linear.x = 0
            vel_msg.angular.z = -turn
            print("Right we go")
        else:
            vel_msg.linear.x = 0
            vel_msg.angular.z = 0
            print("Parking")

        pub.publish(vel_msg)
        rate.sleep()

# Main function
if __name__ == '__main__':
    try:
        # Save terminal settings
        settings = termios.tcgetattr(sys.stdin)

        # Run moveRobot function
        moveRobot()

    except rospy.ROSInterruptException:
        pass

    finally:
        # Restore terminal settings
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
