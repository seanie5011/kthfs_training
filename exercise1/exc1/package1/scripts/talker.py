#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16

def talker():
    # assign topic and datatype, along with queue size
    pub = rospy.Publisher('oriordan', Int16, queue_size=10)
    # initialise node
    rospy.init_node('talker', anonymous=True)
    # define rate
    rate = rospy.Rate(20)  # 20hz

    # k is the value we want to broadcast
    # n is the value affecting it
    k = 0
    n = 4

    # loop while we are still live
    while not rospy.is_shutdown():
        # log the value and publish to topic
        rospy.loginfo(k)
        pub.publish(k)
        # increase by n
        k += n
        # sleep for rate in s
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
