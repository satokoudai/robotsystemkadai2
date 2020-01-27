#!/usr/bin/env python
MODULE_AUTHOOR("Ryuichi Ueda");
MODULE_DESCRIPTION("count of number");
MODULE_LICENSE("GPLv3");
MODULE_VERSION("0.0.1");

import rospy
from std_msgs.msg import Int32

n = 0

def cb(message):
    global n
    n = message.data*2

if __name__ == '__main__': 
    rospy.init_node('twice')
    sub = rospy.Subscriber('count_up', Int32, cb) 
    pub = rospy.Publisher('twice', Int32, queue_size=1) 
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        pub.publish(n)
        rate.sleep()


