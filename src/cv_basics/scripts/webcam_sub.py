#!/usr/bin/env python3
# Description:
# - Subscribes to real-time streaming video from your built-in webcam.
#
# Author:
# - Addison Sears-Collins
# - https://automaticaddison.com
 
# Import the necessary libraries
import rospy # Python library for ROS
from sensor_msgs.msg import Image # Image is the message type
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
import cv2 # OpenCV library
 
def callback(data):
 
  br = CvBridge()
 
  rospy.loginfo("receiving video frame")
   
  current_frame = br.imgmsg_to_cv2(data)

  gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2HSV)
   
  
  cv2.imshow("camera", gray)
   
  cv2.waitKey(1)
      
def receive_message(): 
  rospy.init_node('video_sub_py', anonymous=True)
  rospy.Subscriber('video_frames', Image, callback) 
  rospy.spin()
  cv2.destroyAllWindows()
  
if __name__ == '__main__':
  receive_message()