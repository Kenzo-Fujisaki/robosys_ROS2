#!/bin/bash
# SPDX-FileCopyrightText: 2022 Kenzo Fujisaki
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
ros2 launch robosys_ROS2 omikuji.launch.py > /tmp/robosys_ROS2.log

cat /tmp/robosys_ROS2.log | grep 吉