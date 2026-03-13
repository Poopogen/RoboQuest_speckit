# Feature Specification: API Gateway

**Feature Branch**: `[spec-api-gateway]`  
**Created**: 2026-03-13  
**Status**: Draft  
**Input**: User description: "Detailed spec for REST + WebSocket gateway"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Real-Time VR Event Delivery (Priority: P1)

VR Client 透過 WebSocket 發送事件，API Gateway 即時轉發至後端服務。

**Why this priority**: 事件即時性直接影響機器人與 VR 的同步體驗。

**Independent Test**: 單一 client 發送事件並在 150ms 內收到 ACK。

**Acceptance Scenarios**:

1. **Given** WebSocket 已建立，**When** VR 發送事件，**Then** Gateway 回傳 ACK 並轉發。

---

### User Story 2 - Authenticated REST Access (Priority: P2)

管理端與遊戲服務透過 REST 取得狀態與操作資源。

**Why this priority**: REST 是非即時管理與監控的基礎。

**Independent Test**: JWT 驗證通過後取得 session 狀態。

**Acceptance Scenarios**:

1. **Given** 有效 JWT，**When** 呼叫 /sessions/{id}，**Then** 回傳 session 狀態與最後事件時間。

---

### User Story 3 - Rate Limiting & Backpressure (Priority: P3)

系統在高流量時提供降速與回復策略。

**Why this priority**: 在多玩家與大量事件時避免後端過載。

**Independent Test**: 模擬高頻事件並得到 429 或 backpressure 訊號。

**Acceptance Scenarios**:

1. **Given** 事件超過限制，**When** 新事件送出，**Then** 回覆限流錯誤並保留重試建議。

---

### Edge Cases

- WebSocket 連線掉線後重連。
- REST endpoint 呼叫超時。
- 大型 payload 觸發大小限制。

## Requirements *(mandatory)*

### Functional Requirements

- **API-FR-001**: Gateway MUST support WebSocket event ingestion with ACK.
- **API-FR-002**: Gateway MUST provide REST endpoints for sessions, robots, mapping.
- **API-FR-003**: Gateway MUST enforce JWT authentication for REST and WebSocket.
- **API-FR-004**: Gateway MUST apply rate limiting and backpressure.
- **API-FR-005**: Gateway MUST emit structured logs for all requests.

### Key Entities *(include if feature involves data)*

- **SessionStatus**: session_id、最後事件時間、玩家狀態。
- **GatewayEvent**: event_id、payload、ACK 狀態。
- **AuthToken**: user_id、roles、expiry。

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 99% WebSocket ACKs returned within 150ms.
- **SC-002**: REST p95 latency < 200ms for session read endpoints.
- **SC-003**: Rate limiting prevents backend overload under 2x expected load.
- **SC-004**: Authentication error rate < 1% for valid tokens.
