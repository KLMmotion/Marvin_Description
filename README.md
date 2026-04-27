# Robot Description

This repository contains robot description assets for simulation and visualization.

Included robot models:

- Gento Luna
- marvin_pro

The repository provides URDF files, MJCF files, and STL meshes that can be used with ROS-related tools, MuJoCo, and other robot model workflows.

## Repository Structure

```text
Robot_Description/
├─ meshes/
│  ├─ Gento Luna/
│  │  └─ meshes/
│  └─ marvin_pro/
│     └─ meshes/
│        ├─ base/
│        ├─ m3/
│        ├─ m6/
│        ├─ omnigripper/
│        └─ SRS/
├─ mjcf/
│  ├─ Gento Luna/
│  │  └─ Gento Luna.xml
│  └─ marvin_pro/
│     └─ marvin_pro_mink_with_gripper.xml
└─ urdf/
   ├─ Gento Luna/
   │  └─ Gento Luna_URDF.urdf
   └─ marvin_pro/
      └─ marvin_robot.urdf
```

## Models

### Gento Luna

- URDF: `urdf/Gento Luna/Gento Luna_URDF.urdf`
- MJCF: `mjcf/Gento Luna/Gento Luna.xml`
- Meshes: `meshes/Gento Luna/meshes/*.STL`

This model includes the base, leg chain, dual arms, and head links.

### marvin_pro

- URDF: `urdf/marvin_pro/marvin_robot.urdf`
- MJCF: `mjcf/marvin_pro/marvin_pro_mink_with_gripper.xml`
- Meshes: `meshes/marvin_pro/meshes/`

This model includes a base, dual arms, and gripper-related assets.

## File Types

- URDF: robot structure, joints, inertial data, and mesh references
- MJCF: MuJoCo simulation models and assets
- STL meshes: geometry for visual and collision use

## Usage

Use the URDF files with ROS or any URDF-compatible viewer:

- `urdf/Gento Luna/Gento Luna_URDF.urdf`
- `urdf/marvin_pro/marvin_robot.urdf`

Use the MJCF files with MuJoCo-compatible tools:

- `mjcf/Gento Luna/Gento Luna.xml`
- `mjcf/marvin_pro/marvin_pro_mink_with_gripper.xml`

Keep the current folder structure unchanged, because the URDF and MJCF files use relative mesh paths.

## Notes

- Mesh references are relative.
- File names keep the original naming style, including spaces and uppercase `.STL` extensions.
- This repository contains description assets only, not controllers or full simulation projects.
