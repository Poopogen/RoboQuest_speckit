# Feature Specification: Backend Services

**Feature Branch**: `[spec-backend-services]`  
**Created**: 2026-03-13  
**Status**: Draft  
**Input**: User description: "Detailed spec for Game Service, Matchmaking, Environment Analyzer, Object Mapping, Robot Dispatcher"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - End-to-End Dispatch Pipeline (Priority: P1)

後端接收 VR 事件後執行物件映射並派遣機器人送達。

**Why this priority**: 這是平台核心功能鏈路。

**Independent Test**: 模擬事件 → Object Mapping → Robot Dispatcher 並回傳成功。

**Acceptance Scenarios**:

1. **Given** VR 事件進入 Game Service，**When** Object Mapping 完成，**Then** Robot Dispatcher 發出任務並回覆狀態。

---

### User Story 2 - Environment-Aware Mapping (Priority: P2)

Environment Analyzer 解析掃描結果並生成場景 embedding，Object Mapping 查詢 Qdrant 建議實體物件。

**Why this priority**: 支援環境自適應遊戲是核心差異化。

**Independent Test**: 上傳掃描 → 取得 mapping 建議列表。

**Acceptance Scenarios**:

1. **Given** 環境掃描資料，**When** Analyzer 完成 embedding，**Then** Object Mapping 回傳建議物件列表。

---

### User Story 3 - Matchmaking by Environment & Robot Capability (Priority: P3)

系統根據房間大小、可用物件與機器人能力進行配對。

**Why this priority**: 多玩家配對可延後，但需規劃機制。

**Independent Test**: 輸入三個玩家環境描述，返回匹配組合。

**Acceptance Scenarios**:

1. **Given** 玩家 A/B/C 環境資料，**When** 觸發配對，**Then** Matchmaking 返回最佳組合與原因。

---

### Edge Cases

- Object Mapping 找不到符合物件。
- Robot Dispatcher 任務衝突與排隊。
- 缺乏實體機器人時改以模擬回應驗證派遣流程。
- 環境掃描重複導致 embedding 覆蓋。
- Matchmaking 無法形成可行組合。

## Requirements *(mandatory)*

### Functional Requirements

- **BE-FR-001**: Game Service MUST normalize VR events and forward to Robot Dispatcher.
- **BE-FR-002**: Environment Analyzer MUST create scene embeddings and store in Qdrant.
- **BE-FR-003**: Object Mapping MUST map VR objects to real objects using VLM prompts.
- **BE-FR-004**: Robot Dispatcher MUST queue and schedule tasks with retry and timeout.
- **BE-FR-005**: Matchmaking MUST consider room size, objects, and robot capability.
- **BE-FR-006**: Backend MUST provide simulated robot dispatch responses when hardware is unavailable.

### Key Entities *(include if feature involves data)*

- **DispatchTask**: 任務 ID、目標位置、payload、狀態。
- **EnvironmentSnapshot**: 場景 metadata、embedding、時間戳。
- **ObjectMapping**: VR object → real object 對映結果。
- **MatchConfig**: 玩家列表、配對結果、條件。

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Backend dispatch pipeline p95 end-to-end < 2s (event → dispatch ACK).
- **SC-002**: 95% of mapping requests return a valid object candidate list.
- **SC-003**: Robot task queue handles 50 concurrent tasks with <5% delay beyond SLA.
- **SC-004**: Matchmaking completes within 3s for 95% of requests.
- **SC-005**: Simulated dispatch flows cover 100% of failure/success paths in tests.
