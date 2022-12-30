# SPDX-FileCopyrightText: 2022 Kenzo Fujisaki
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
import random

class Fortune():
    def __init__(self, node):
        self.pub = node.create_publisher(Int16, "number", 10)
        self.num = random.randint(1,100)
        print("引いた番号は:" + str(self.num))
        node.create_timer(2, self.cb)

    def cb(self):
        msg = Int16()
        msg.data = self.num
        self.pub.publish(msg)

def main():
    rclpy.init()
    node = Node("fortune")
    fortune = Fortune(node)
    rclpy.spin_once(node)

if __name__ == '__main__':
    main()