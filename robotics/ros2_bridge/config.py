from dataclasses import dataclass


@dataclass
class Ros2BridgeConfig:
    simulation: bool = True
    dispatch_topic: str = "/dispatch/goal_pose"
    telemetry_topic: str = "/telemetry/robot_state"
