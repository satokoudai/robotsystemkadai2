#!/usr/bin/env python
MODULE_AUTHOOR("Ryuichi Ueda");
MODULE_DESCRIPTION("count of number");
MODULE_LICENSE("GPLv3");
MODULE_VERSION("0.0.1");



import rospy
from std_msgs.msg import Int32

if __name__ == '__main__':
    rospy.init_node('count')
    pub = rospy.Publisher('count_up', Int32, queue_size=1)
    rate = rospy.Rate(10)
    n = 0
    while not rospy.is_shutdown():
        n += 1
        pub.publish(n)
        rate.sleep()
