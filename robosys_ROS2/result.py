# SPDX-FileCopyrightText: 2022 Kenzo Fujisaki
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

def cb(msg):
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


rclpy.init()
node = Node("result")
pub = node.create_subscription(Int16, "number", cb, 10)
rclpy.spin(node)