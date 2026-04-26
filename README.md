# Marvin_Description

ROS 2 robot description package for the **Marvin** mobile manipulation platform by [KLMmotion](https://github.com/KLMmotion).

This package contains the URDF/Xacro robot model, meshes, launch files, and RViz configuration needed to visualise Marvin in RViz and simulate it in Gazebo.

---

## Overview

| Field | Value |
|---|---|
| Robot name | Marvin |
| ROS version | ROS 2 (Humble / Iron / Jazzy) |
| License | Apache-2.0 |
| Maintainer | KLMmotion |

Marvin is a differential-drive mobile base with an integrated sensor suite (2-D LiDAR, RGB-D camera, IMU). The description package models the full kinematic chain and collision geometry used by the navigation stack, MoveIt 2, and simulation environments.

---

## Package structure

```
marvin_description/
├── config/
│   └── marvin.rviz            # RViz 2 display configuration
├── launch/
│   └── display.launch.py      # Launches robot_state_publisher + RViz 2
├── meshes/
│   ├── collision/             # Simplified collision meshes (.stl)
│   └── visual/                # High-resolution visual meshes (.dae / .stl)
├── urdf/
│   ├── marvin.urdf.xacro      # Top-level robot entry point
│   ├── marvin_base.urdf.xacro # Mobile base geometry and joints
│   └── sensors.urdf.xacro     # Sensor frames (LiDAR, camera, IMU)
├── CMakeLists.txt
└── package.xml
```

---

## Dependencies

- `robot_state_publisher`
- `joint_state_publisher_gui`
- `xacro`
- `rviz2`

Install them with:

```bash
sudo apt install ros-$ROS_DISTRO-robot-state-publisher \
                 ros-$ROS_DISTRO-joint-state-publisher-gui \
                 ros-$ROS_DISTRO-xacro \
                 ros-$ROS_DISTRO-rviz2
```

---

## Building

```bash
# Inside your ROS 2 workspace
cd ~/ros2_ws/src
git clone https://github.com/KLMmotion/Marvin_Description.git marvin_description
cd ~/ros2_ws
rosdep install --from-paths src --ignore-src -r -y
colcon build --packages-select marvin_description
source install/setup.bash
```

---

## Visualising the robot

```bash
ros2 launch marvin_description display.launch.py
```

This opens RViz 2 with the full robot model and a Joint State Publisher GUI so you can interactively move the joints.

---

## URDF / Xacro arguments

The top-level xacro file (`marvin.urdf.xacro`) exposes the following arguments:

| Argument | Default | Description |
|---|---|---|
| `use_sim_time` | `false` | Set to `true` when running in simulation |
| `namespace` | `""` | Optional TF namespace prefix |

Example:

```bash
xacro urdf/marvin.urdf.xacro use_sim_time:=true namespace:=robot1
```

---

## License

Copyright 2024 KLMmotion. Licensed under the [Apache License 2.0](LICENSE).
