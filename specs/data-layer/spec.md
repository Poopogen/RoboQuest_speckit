# Feature Specification: Data Layer

**Feature Branch**: `[spec-data-layer]`  
**Created**: 2026-03-13  
**Status**: Draft  
**Input**: User description: "Detailed spec for PostgreSQL, Redis, Dataset Storage, Qdrant"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Persist Session & Dispatch Data (Priority: P1)

系統需要持久化 session、事件與派遣任務資料。

**Why this priority**: 持久化是可追溯與監控的基礎。

**Independent Test**: 建立 session 後可查詢事件與派遣歷史。

**Acceptance Scenarios**:

1. **Given** 新 session，**When** 事件與任務發生，**Then** PostgreSQL 可查詢完整記錄。

---

### User Story 2 - Fast State Cache (Priority: P2)

使用 Redis 快取即時狀態，提供 API 即時回應。

**Why this priority**: 降低 latency，支援即時 UX。

**Independent Test**: cache miss → load from DB → cache hit within 50ms。

**Acceptance Scenarios**:

1. **Given** Redis cache 存在，**When** 查詢 session 狀態，**Then** 回傳結果小於 50ms。

---

### User Story 3 - Scene Embedding Storage (Priority: P3)

Qdrant 儲存場景與物件 embedding，支援 Object Mapping。

**Why this priority**: 需要維持環境記憶以避免重複分析。

**Independent Test**: 存入 embedding 後可用相似度查詢。

**Acceptance Scenarios**:

1. **Given** 新場景 embedding，**When** 查詢相似度，**Then** 回傳 top-k 候選。

---

### Edge Cases

- Redis 資料過期導致狀態回退。
- Qdrant index 重建導致短暫不可用。
- Dataset storage 空間不足。

## Requirements *(mandatory)*

### Functional Requirements

- **DL-FR-001**: Data Layer MUST persist sessions, events, dispatch tasks in PostgreSQL.
- **DL-FR-002**: Data Layer MUST provide Redis cache for real-time state.
- **DL-FR-003**: Data Layer MUST store embeddings and metadata in Qdrant.
- **DL-FR-004**: Dataset storage MUST keep raw scans and telemetry artifacts.
- **DL-FR-005**: Data Layer MUST provide retention and cleanup policies.

### Key Entities *(include if feature involves data)*

- **SessionRecord**: session_id、玩家資訊、時間戳。
- **DispatchRecord**: 任務狀態、Robot 回報。
- **EmbeddingRecord**: vector、metadata、source。
- **DatasetArtifact**: 檔案路徑、類型、版本。

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 99% of session reads served within 200ms.
- **SC-002**: Redis cache hit ratio ≥ 90% for active sessions.
- **SC-003**: Embedding query p95 < 500ms for top-k search.
- **SC-004**: Dataset storage maintains 30-day retention with <1% data loss.
