# SPDX-FileCopyrightText: 2022 Kenzo Fujisaki
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Result():
    def __init__(self,node):
        self.pub = node.create_subscription(Int16, "number", self.cb, 10)

    def cb(self,msg):
        omikuji = msg.data

        if 1 <= omikuji <= 10:
            f = open('/home/kenzo-fujisaki/ros2_ws/src/robosys_ROS2/robosys_ROS2/omikujibox/daikichi.txt','r')
            data = f.read()
            print(data)
        elif 11 <= omikuji <= 35:
            f = open('/home/kenzo-fujisaki/ros2_ws/src/robosys_ROS2/robosys_ROS2/omikujibox/kichi.txt','r')
            data = f.read()
            print(data)
        elif 36 <= omikuji <= 60:
            f = open('/home/kenzo-fujisaki/ros2_ws/src/robosys_ROS2/robosys_ROS2/omikujibox/tyuukichi.txt','r')
            data = f.read()
            print(data)
        elif 61 <= omikuji <= 75:
            f = open('/home/kenzo-fujisaki/ros2_ws/src/robosys_ROS2/robosys_ROS2/omikujibox/syoukichi.txt','r')
            data = f.read()
            print(data)
        elif 76 <= omikuji <= 85:
            f = open('/home/kenzo-fujisaki/ros2_ws/src/robosys_ROS2/robosys_ROS2/omikujibox/suekichi.txt','r')
            data = f.read()
            print(data)
        elif 86 <= omikuji <= 95:
            f = open('/home/kenzo-fujisaki/ros2_ws/src/robosys_ROS2/robosys_ROS2/omikujibox/kyou.txt','r')
            data = f.read()
            print(data)
        elif 96 <= omikuji <= 100:
            f = open('/home/kenzo-fujisaki/ros2_ws/src/robosys_ROS2/robosys_ROS2/omikujibox/daikyou.txt','r')
            data = f.read()
            print(data)

def main():
    rclpy.init()
    node = Node("result")
    result = Result(node)
    rclpy.spin_once(node)

if __name__ == '__main__':
    main()