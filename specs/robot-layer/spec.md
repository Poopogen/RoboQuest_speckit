# Feature Specification: Robot Layer

**Feature Branch**: `[spec-robot-layer]`  
**Created**: 2026-03-13  
**Status**: Draft  
**Input**: User description: "Detailed spec for Robot Control Service, ROS2 Bridge, TurtleBot3, Navigation Stack"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Execute Navigation Task (Priority: P1)

Robot Control Service 接收 dispatch 任務，透過 ROS2 Bridge 下達導航指令，TurtleBot 到達目標點。

**Why this priority**: 實體機器人導航是 mixed-reality 的關鍵能力。

**Independent Test**: 模擬導航目標，確認 ROS2 goal_pose 發出並回報到達。

**Acceptance Scenarios**:

1. **Given** 新 dispatch 任務，**When** 目標下達，**Then** Robot 回報導航成功。

---

### User Story 2 - Payload Delivery & Acknowledgement (Priority: P2)

Robot 搭載物件並在指定點停靠後回報任務完成。

**Why this priority**: 物件遞送完成確認是 VR 更新的依據。

**Independent Test**: 模擬 payload 任務，確認完成狀態上傳。

**Acceptance Scenarios**:

1. **Given** 任務包含 payload，**When** Robot 到達目標點，**Then** 回傳 delivery 完成事件。

---

### User Story 3 - Safety & Collision Avoidance (Priority: P3)

Robot 行走過程中即時避障並回報異常。

**Why this priority**: 安全性很重要但可在核心導航之後實作。

**Independent Test**: 模擬障礙物，確認導航 stack 重新規劃路徑。

**Acceptance Scenarios**:

1. **Given** 障礙物出現，**When** Robot 接近，**Then** Navigation Stack 重新規劃並回報。

---

### Edge Cases

- ROS2 Bridge 斷線。
- 無實體 TurtleBot 時使用模擬 ROS2 節點回放。
- Navigation Stack 無法到達目標。
- Robot 電量不足。

## Requirements *(mandatory)*

### Functional Requirements

- **RB-FR-001**: Robot Control Service MUST translate dispatch tasks into ROS2 actions.
- **RB-FR-002**: ROS2 Bridge MUST provide telemetry feedback to backend.
- **RB-FR-003**: Robot MUST acknowledge task completion and failure states.
- **RB-FR-004**: Navigation Stack MUST support dynamic obstacle avoidance.
- **RB-FR-005**: Robot Layer MUST report battery and health status.
- **RB-FR-006**: Robot Layer MUST support simulation mode with ROS2 mock topics/actions when TurtleBot hardware is unavailable.

### Key Entities *(include if feature involves data)*

- **RobotState**: 位置、速度、電量、任務狀態。
- **NavigationGoal**: 目標座標、路徑、時間戳。
- **TelemetryPacket**: sensor data、狀態更新。

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 95% navigation goals completed within SLA (5s for short range).
- **SC-002**: Telemetry update interval < 500ms for active tasks.
- **SC-003**: Collision avoidance success rate ≥ 98% in test scenarios.
- **SC-004**: Robot health status updates available within 2s of change.
- **SC-005**: Simulated ROS2 pipeline reproduces dispatch success/failure paths for 100% of test cases.
