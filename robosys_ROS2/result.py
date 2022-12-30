# SPDX-FileCopyrightText: 2022 Kenzo Fujisaki
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

def cb(msg):
    omikuji = msg.data

    if omikuji == 1:
        f = open('/home/kenzo-fujisaki/ros2_ws/src/robosys_ROS2/robosys_ROS2/daikichi.txt','r')
        data = f.read()
        print(data)
    elif omikuji == 2:
        f = open('/home/kenzo-fujisaki/ros2_ws/src/robosys_ROS2/robosys_ROS2/kichi.txt','r')
        data = f.read()
        print(data)
    elif omikuji == 3:
        f = open('/home/kenzo-fujisaki/ros2_ws/src/robosys_ROS2/robosys_ROS2/tyuukichi.txt','r')
        data = f.read()
        print(data)
    elif omikuji == 4:
        f = open('/home/kenzo-fujisaki/ros2_ws/src/robosys_ROS2/robosys_ROS2/syouichi.txt','r')
        data = f.read()
        print(data)
    elif omikuji == 5:
        f = open('/home/kenzo-fujisaki/ros2_ws/src/robosys_ROS2/robosys_ROS2/suekichi.txt','r')
        data = f.read()
        print(data)
    elif omikuji == 6:
        f = open('/home/kenzo-fujisaki/ros2_ws/src/robosys_ROS2/robosys_ROS2/kyou.txt','r')
        data = f.read()
        print(data)
    elif omikuji == 7:
        f = open('/home/kenzo-fujisaki/ros2_ws/src/robosys_ROS2/robosys_ROS2/daikyou.txt','r')
        data = f.read()
        print(data)


rclpy.init()
node = Node("result")
pub = node.create_subscription(Int16, "number", cb, 10)
rclpy.spin(node)