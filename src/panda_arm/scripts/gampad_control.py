#!/usr/bin/env python
from inputs import get_gamepad
import rospy
from std_msgs.msg import Float64

rospy.init_node('gamepad_control')

#joint    min     max
#joint1  -2.90   2.90
#joint2  -1.76   1.76
#joint3  -2.90   2.90
#joint4  -3.07   0.02
#joint5  -2.90   2.90
#joint6  -0.02   3.75
#joint7  -2.90   -2.90
#finger   0.0    0.04

joint1 = 127.5
joint2 = 127.5
joint3 = 127.5
joint4 = 127.5
joint5 = 127.5
joint6 = 127.5
joint7 = 127.5


joint1_pub = rospy.Publisher('/arm_position_controller/panda_joint1_position_controller/command', Float64, queue_size=10)
joint2_pub = rospy.Publisher('/arm_position_controller/panda_joint2_position_controller/command', Float64, queue_size=10)
joint3_pub = rospy.Publisher('/arm_position_controller/panda_joint3_position_controller/command', Float64, queue_size=10)
joint4_pub = rospy.Publisher('/arm_position_controller/panda_joint4_position_controller/command', Float64, queue_size=10)
joint5_pub = rospy.Publisher('/arm_position_controller/panda_joint5_position_controller/command', Float64, queue_size=10)
joint6_pub = rospy.Publisher('/arm_position_controller/panda_joint6_position_controller/command', Float64, queue_size=10)
joint7_pub = rospy.Publisher('/arm_position_controller/panda_joint7_position_controller/command', Float64, queue_size=10)



def translate(value, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = float(value - leftMin) / float(leftSpan)
    return rightMin + (valueScaled * rightSpan)



while not rospy.is_shutdown():
    events = get_gamepad()
    for event in events:
        # print(event.code, event.state)
        if event.code == 'ABS_Y':
            if event.state == 0:
                joint1 = joint1 + 3
                if joint1 > 255:
                    joint1 = 255
                    print("JOINT_1 MAX JOINT REACHED")
                print("JOINT 1: ",translate(joint1,0,255,-2.90,2.90))  
                joint1_pub.publish(translate(joint1,0,255,-2.90,2.90)) 
            elif event.state == 255:
                joint1 = joint1 - 3
                if joint1 < 0:
                    joint1 = 0
                    print("JOINT_1 MIN JOINT REACHED")
                print("JOINT 1: ",translate(joint1,0,255,-2.90,2.90))  
                joint1_pub.publish(translate(joint1,0,255,-2.90,2.90)) 
                          
                          
        elif event.code == 'ABS_X':
            if event.state == 0:
                joint2 = joint2 + 3
                if joint2 > 255:
                    joint2 = 255
                    print("JOINT_2 MAX JOINT REACHED")
                print("JOINT 2: ",translate(joint2,0,255,-1.76,1.76))   
                joint2_pub.publish(translate(joint2,0,255,-1.76,1.76))
            elif event.state == 255:
                joint2 = joint2 - 3
                if joint2 < 0:
                    joint2 = 0
                    print("JOINT_2 MIN JOINT REACHED")
                print("JOINT 2: ",translate(joint2,0,255,-1.76,1.76))
                joint2_pub.publish(translate(joint2,0,255,-1.76,1.76))

        
        elif event.code == 'BTN_TOP2':
            if event.state == 1:
                joint5 = joint5 + 3
                if joint5 > 255:
                    joint5 = 255
                    print("JOINT_5 MAX JOINT REACHED")
                print("JOINT 5: ",translate(joint5,0,255,-2.90,2.90))
                joint5_pub.publish(translate(joint5,0,255,-2.90,2.90))
        
        elif event.code == 'BTN_BASE':
            if event.state == 1:
                joint5 = joint5 - 3
                if joint5 < 0:
                    joint5 = 0
                    print("JOINT_5 MIN JOINT REACHED")
                print("JOINT 5: ",translate(joint5,0,255,-2.90,2.90))
                joint5_pub.publish(translate(joint5,0,255,-2.90,2.90))

            
        elif event.code == 'BTN_TRIGGER':
            if event.state == 1:
                joint3 = joint3 + 3
                if joint3 > 255:
                    joint3 = 255
                    print("JOINT_3 MAX JOINT REACHED")
                print("JOINT 3: ",translate(joint3,0,255,-2.90,2.90))
                joint3_pub.publish(translate(joint3,0,255,-2.90,2.90))
                
        elif event.code == 'BTN_THUMB2':
            if event.state == 1:
                joint3 = joint3 - 3
                if joint3 < 0:
                    joint3 = 0
                    print("JOINT_3 MIN JOINT REACHED")
                print("JOINT 3: ",translate(joint3,0,255,-2.90,2.90))
                joint3_pub.publish(translate(joint3,0,255,-2.90,2.90))
            
        elif event.code == 'BTN_THUMB':
            if event.state == 1:
                joint4 = joint4 - 3
                if joint4 > 255:
                    joint4 = 255
                    print("JOINT_4 MAX JOINT REACHED")
                print("JOINT 4: ",translate(joint4,0,255,-3.07,0.02))
                joint4_pub.publish(translate(joint4,0,255,-3.07,0.02))
        
        elif event.code == 'BTN_TOP':
            if event.state == 1:
                joint4 = joint4 + 3
                if joint4 < 0:
                    joint4 = 0
                    print("JOINT_4 MIN JOINT REACHED")
                print("JOINT 4: ",translate(joint4,0,255,-3.07,0.02))
                joint4_pub.publish(translate(joint4,0,255,-3.07,0.02))
                
        elif event.code == 'BTN_PINKIE':
            if event.state == 1:
                joint6 = joint6 + 3
                if joint6 > 255:
                    joint6 = 255
                    print("JOINT_6 MAX JOINT REACHED")
                print("JOINT 6: ",translate(joint6,0,255,-0.02,3.750))
                joint6_pub.publish(translate(joint6,0,255,-0.02,3.750))
        
        elif event.code == 'BTN_BASE2':
            if event.state == 1:
                joint6 = joint6 - 3
                if joint6 < 0:
                    joint6 = 0
                    print("JOINT_6 MIN JOINT REACHED")
                print("JOINT 6: ",translate(joint6,0,255,-0.02,3.75))
                joint6_pub.publish(translate(joint6,0,255,-0.02,3.750))
                
        elif event.code == 'BTN_BASE3':
            if event.state == 1:
                joint7 = joint7 + 3
                if joint7 > 255:
                    joint7 = 255
                    print("JOINT_7 MAX JOINT REACHED")
                print("JOINT 7: ",translate(joint7,0,255,-2.90,2.90))
                joint7_pub.publish(translate(joint7,0,255,-2.90,2.90))
        
        elif event.code == 'BTN_BASE4':
            if event.state == 1:
                joint7 = joint7 - 3
                if joint7 < 0:
                    joint7 = 0
                    print("JOINT_7 MIN JOINT REACHED")
                print("JOINT 7: ",translate(joint7,0,255,-2.90,2.90))
                joint7_pub.publish(translate(joint7,0,255,-2.90,2.90))


    rospy.sleep(0.01)          
# input_value = -90  # Example input value from 0 to 255
# mapped_value = translate(input_value, 0, 255, -2.90, 2.90)
# print(mapped_value)
 
 
