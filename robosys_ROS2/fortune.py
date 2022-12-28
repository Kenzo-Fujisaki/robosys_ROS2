# SPDX-FileCopyrightText: 2022 Kenzo Fujisaki
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
import random

class Fortune():
    def __init__(self,node):
        self.pub = node.create_publisher(Int16, "number", 10)

    def cb(self):
        num = random.randint(1,7)
        self.pub.publish(num)

def main():
    rclpy.init()
    node = Node("fortune")
    fortune = Fortune(node)
    rclpy.spin(node)

if __name__ == '__main__':
    main()