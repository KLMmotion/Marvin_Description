# Robot Description

Robot description assets for three robots: Gento Luna, Gento Skye, and marvin_pro.

This repository contains URDF files, MuJoCo MJCF files, and STL meshes for visualization, simulation, and robot model conversion workflows.

## Structure

```text
Robot_Description/
+-- urdf/      # URDF robot models
+-- mjcf/      # MuJoCo MJCF robot models
+-- meshes/    # STL mesh assets
```

## Robots

### Gento Luna

- URDF: `urdf/Gento Luna/Gento Luna_URDF.urdf`
- MJCF: `mjcf/Gento Luna/Gento Luna.xml`
- Meshes: `meshes/Gento Luna/meshes/`

### Gento Skye

- URDF: `urdf/Gento Skye/Gento Skye_URDF.urdf`
- MJCF: `mjcf/Gento Skye/Gento_Skye_URDF.xml`
- Meshes: `meshes/Gento Skye/meshes/`

### marvin_pro

URDF:

- No gripper: `urdf/marvin_pro/marvin_robot.urdf`
- Parallel gripper: `urdf/marvin_pro/marvin_pro_mink_with_gripper.urdf`
- 45-degree downward gripper: `urdf/marvin_pro/marvin_pro_mink_with_45gripper.urdf`

MJCF:

- No gripper: `mjcf/marvin_pro/marvin_pro_mink.xml`
- Parallel gripper: `mjcf/marvin_pro/marvin_pro_mink_with_gripper.xml`
- 45-degree downward gripper: `mjcf/marvin_pro/marvin_pro_mink_with_45gripper.xml`

Meshes:

- `meshes/marvin_pro/meshes/base/`
- `meshes/marvin_pro/meshes/m3/`
- `meshes/marvin_pro/meshes/m6/`
- `meshes/marvin_pro/meshes/omnigripper/`
- `meshes/marvin_pro/meshes/45omnigripper/`
- `meshes/marvin_pro/meshes/SRS/`

## Notes

- URDF files can be used with ROS, RViz, and URDF-compatible viewers.
- MJCF files can be used with MuJoCo.
- Mesh paths are relative, so keep the repository structure unchanged.
- This repository contains robot description assets only. It does not include controllers, launch files, or complete simulation projects.