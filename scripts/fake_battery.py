#!/usr/bin/env python
import random
import rospy
from sensor_msgs.msg import BatteryState

if __name__ == "__main__":
    rospy.init_node("fake_battery", anonymous = True)
    fake_battery_publisher = rospy.Publisher("battery_status", BatteryState, queue_size = 10)

    r = rospy.Rate(1)
    r.sleep()
    while not rospy.is_shutdown():
        battery_msg = BatteryState()

        battery_msg.percentage = round(random.uniform(0.95, 0.98), 2)
        fake_battery_publisher.publish(battery_msg)

        r.sleep()
