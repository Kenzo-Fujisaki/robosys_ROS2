# SPDX-FileCopyrightText: 2022 Kenzo Fujisaki
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
import random

rclpy.init()
node = Node("fortune")
pub = node.create_publisher(Int16, "number", 10)
num = random.randint(1,7)

def cb():
    global num
    msg = Int16()
    msg.data = num
    pub.publish(msg)

node.create_timer(0.5, cb)
rclpy.spin(node)
