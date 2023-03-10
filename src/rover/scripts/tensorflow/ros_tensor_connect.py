#!/usr/bin/env python3
from __future__ import print_function
from tensor import *


import roslib
roslib.load_manifest('rover')
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class image_converter:

  def __init__(self):
    self.image_pub = rospy.Publisher("image_topic_2",Image)

    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/camera1/image_raw",Image,self.callback)

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)

    output = detect_object(cv_image)

    cv2.imshow("Image window",output)
    cv2.waitKey(3)

      
    try:
      self.image_pub.publish(self.bridge.cv2_to_imgmsg(output, "bgr8"))
    except CvBridgeError as e:
      print(e)

 


def main(args):
  ic = image_converter()
  rospy.init_node('image_converter', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)