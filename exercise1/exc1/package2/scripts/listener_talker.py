#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16, Float32

def callback(data):
    # result is this data divided by q
    q = 0.15
    result = float(data.data) / q

    # assign topic and datatype, along with queue size
    pub = rospy.Publisher('kthfs/result', Float32, queue_size=10)

    # log the result and publish to topic
    rospy.loginfo(result)
    pub.publish(result)

def listener_talker():
    # initialise the node
    rospy.init_node('listener', anonymous=False)
    # subscribe to topic
    rospy.Subscriber('oriordan', Int16, callback)
    # do not exit until shutdown
    rospy.spin()

if __name__ == '__main__':
    listener_talker()
