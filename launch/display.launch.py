"""display.launch.py

Launch the Marvin robot description in RViz 2.

Nodes started
-------------
* robot_state_publisher  – publishes /tf from the URDF and /robot_description
* joint_state_publisher_gui – provides an interactive GUI to move joints
* rviz2                  – visualises the robot with a preconfigured view

Usage
-----
ros2 launch marvin_description display.launch.py [use_sim_time:=false] [namespace:='']
"""

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import (
    Command,
    FindExecutable,
    LaunchConfiguration,
    PathJoinSubstitution,
)
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description() -> LaunchDescription:
    pkg_share = get_package_share_directory("marvin_description")

    # ── Declared arguments ────────────────────────────────────────────
    use_sim_time_arg = DeclareLaunchArgument(
        "use_sim_time",
        default_value="false",
        description="Use simulation (Gazebo) clock when true",
    )
    namespace_arg = DeclareLaunchArgument(
        "namespace",
        default_value="",
        description="Optional TF frame namespace prefix",
    )

    use_sim_time = LaunchConfiguration("use_sim_time")
    namespace = LaunchConfiguration("namespace")

    # ── Robot description (xacro → URDF string) ───────────────────────
    xacro_file = PathJoinSubstitution(
        [FindPackageShare("marvin_description"), "urdf", "marvin.urdf.xacro"]
    )
    robot_description = Command(
        [
            FindExecutable(name="xacro"),
            " ",
            xacro_file,
            " use_sim_time:=",
            use_sim_time,
            " namespace:=",
            namespace,
        ]
    )

    # ── Nodes ─────────────────────────────────────────────────────────
    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        name="robot_state_publisher",
        output="screen",
        parameters=[
            {
                "robot_description": robot_description,
                "use_sim_time": use_sim_time,
            }
        ],
    )

    joint_state_publisher_gui_node = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
        name="joint_state_publisher_gui",
        output="screen",
        parameters=[{"use_sim_time": use_sim_time}],
    )

    rviz_config = os.path.join(pkg_share, "config", "marvin.rviz")
    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="screen",
        arguments=["-d", rviz_config],
        parameters=[{"use_sim_time": use_sim_time}],
    )

    return LaunchDescription(
        [
            use_sim_time_arg,
            namespace_arg,
            robot_state_publisher_node,
            joint_state_publisher_gui_node,
            rviz_node,
        ]
    )
