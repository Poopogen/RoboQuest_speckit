# Feature Specification: VR Client Layer

**Feature Branch**: `[spec-vr-client]`  
**Created**: 2026-03-13  
**Status**: Draft  
**Input**: User description: "Detailed spec for VR Client subsystem from DESIGN.md"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Trigger Physical Pickup from VR (Priority: P1)

玩家在 VR 中觸發可拾取物件事件，系統即時發送事件至後端並派遣機器人送達對應實體物件。

**Why this priority**: 核心 mixed-reality 互動必須先可用，才能驗證平台價值。

**Independent Test**: 使用單一 VR 客戶端模擬事件，後端回傳派遣成功，玩家端顯示狀態更新即可驗證。

**Acceptance Scenarios**:

1. **Given** 玩家進入可互動場景，**When** 觸發 `spawn_item` 事件，**Then** VR Client 將事件透過 WebSocket 發送並收到派遣回執。
2. **Given** 事件派遣成功，**When** 實體物件送達，**Then** VR Client 顯示拾取完成並更新能量數值。

---

### User Story 2 - Environment Scan and Object Mapping Sync (Priority: P2)

玩家啟動環境掃描，VR Client 上傳場景資訊供後端建立物件映射。

**Why this priority**: 讓系統具備環境自適應能力，支援非固定場景。

**Independent Test**: 上傳掃描資料並收到後端回應的可映射物件清單。

**Acceptance Scenarios**:

1. **Given** 玩家啟動掃描模式，**When** 掃描完成上傳，**Then** 後端回傳映射建議列表並顯示於 VR 端。

---

### User Story 3 - Coordinate Alignment Calibration (Priority: P3)

玩家依照指引放置 marker 並完成 VR ↔ robot 座標對齊。

**Why this priority**: 坐標對齊支援高精度互動，但可晚於核心互動完成。

**Independent Test**: 以標準校正流程完成後，取得 T_vr_robot 轉換矩陣並存檔。

**Acceptance Scenarios**:

1. **Given** 校正模式啟動，**When** VR Camera 偵測到 marker，**Then** 生成並上傳 transform。

---

### Edge Cases

- VR 設備網路中斷時事件延遲或重送。
- 無實體 VR 裝置時使用模擬輸入驅動事件。
- Marker 偵測失敗導致校正中斷。
- 物件映射列表為空時的 UI 提示。
- VR↔backend 延遲超出 150ms 的降級提示。

## Requirements *(mandatory)*

### Functional Requirements

- **VR-FR-001**: VR Client MUST send game events via WebSocket within 50ms of user action.
- **VR-FR-002**: VR Client MUST upload environment scan payloads with session metadata.
- **VR-FR-003**: VR Client MUST support coordinate alignment using AprilTag/ArUco markers.
- **VR-FR-004**: VR Client MUST render dispatch status updates and tactile parity cues.
- **VR-FR-005**: VR Client MUST cache events and retry on transient network failures.
- **VR-FR-006**: VR Client MUST provide a simulation mode for input, scan, and alignment when no VR hardware is available.

### Key Entities *(include if feature involves data)*

- **PlayerSession**: 玩家連線與裝置識別、場景狀態。
- **VREvent**: 事件名稱、時間戳、VR 座標、payload。
- **EnvironmentScan**: 掃描點雲/影像摘要、場景 metadata。
- **AlignmentTransform**: T_vr_marker、T_marker_robot、T_vr_robot。

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: VR↔backend p95 latency < 150ms for event dispatch.
- **SC-002**: 98% of sessions complete environment scan upload without retry failure.
- **SC-003**: Coordinate alignment completes within 2 minutes for 90% of users.
- **SC-004**: 95% of dispatch events show tactile parity UI feedback.
- **SC-005**: Event retry mechanism succeeds within 3 attempts for 99% of transient failures.
- **SC-006**: Simulation mode reproduces event flows with <5% deviation from hardware logs (once hardware is available).
