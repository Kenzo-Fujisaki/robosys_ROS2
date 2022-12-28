# SPDX-FileCopyrightText: 2022 Kenzo Fujisaki
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

def cb(num):
    global node
    node = num
    if node == 1:
        print("大吉")
    elif node == 2:
        print("吉")
    elif node == 3:
        print("中吉")
    elif node == 4:
        print("小吉")
    elif node == 5:
        print("末吉")
    elif node == 6:
        print("凶")
    elif node == 7:
        print("大凶")

rclpy.init()
node = Node("listener")
pub = node.create_subscription(Int16, "number", cb, 10)
rclpy.spin(node)