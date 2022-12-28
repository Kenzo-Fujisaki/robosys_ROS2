# SPDX-FileCopyrightText: 2022 Kenzo Fujisaki
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
import random

class Fortune():
    def __init__(self, node):
        self.pub = node.create_publisher(Int16, "number", 10)

    def cb(self, node):
        input_key = input()
        print("[N]:おみくじ,[L]:恋みくじ")
        if input_key == 'n':
            normal = random.randint(1,7)
            self.pub.publish(normal)

        elif input_key == 'l':
            love = random.randint(1,7)
            self.pub.publish(love)

        else:
            print("error")
            rclpy.shutdown(node)

def main():
    rclpy.init()
    node = Node("fortune")
    fortune = Fortune()
    rclpy.spin(node)

if __name__ == '__main__':
    main()