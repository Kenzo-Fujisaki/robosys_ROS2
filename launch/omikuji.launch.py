# SPDX-FileCopyrightText: 2022 Kenzo Fujisaki
# SPDX-License-Identifier: BSD-3-Clause

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():
    fortune = launch_ros.actions.Node(
        package='robosys_ROS2',
        executable='fortune',
        output='screen'
        )
    result = launch_ros.actions.Node(
        package='robosys_ROS2',
        executable='result',
        output='screen'
        )

    return launch.LaunchDescription([fortune, result])