# Robot Layer Contract (ROS2)

## Topics

- `/dispatch/goal_pose` (geometry_msgs/PoseStamped)
- `/telemetry/robot_state` (custom msg: RobotState)
- `/telemetry/battery` (std_msgs/Float32)

## Actions

- `/navigate_to_pose` (nav2_msgs/action/NavigateToPose)

## QoS Policies

- Telemetry: best effort, depth 10
- Dispatch: reliable, depth 5

## Simulation Toggle

- `ROS_SIMULATION=true` env flag to enable Gazebo-only mode

## Bridge API

- REST→ROS2 bridge publishes dispatch goals and listens for telemetry.
- Telemetry is fanned out to Redis streams for UI updates.
