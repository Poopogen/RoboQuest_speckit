# Feature Specification: AI Layer

**Feature Branch**: `[spec-ai-layer]`  
**Created**: 2026-03-13  
**Status**: Draft  
**Input**: User description: "Detailed spec for Object Detection/VLM + Scene Understanding"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Object Detection for Mapping (Priority: P1)

AI 模型從環境掃描中偵測可用物件並回傳特徵。

**Why this priority**: Object Mapping 依賴偵測結果。

**Independent Test**: 輸入影像掃描，輸出物件清單與信心分數。

**Acceptance Scenarios**:

1. **Given** 場景掃描影像，**When** 執行偵測，**Then** 回傳物件清單與位置。

---

### User Story 2 - Scene Understanding Embedding (Priority: P2)

系統生成場景 embedding 供 Qdrant 搜尋與對比。

**Why this priority**: 支援場景記憶與相似度查詢。

**Independent Test**: 同一場景多次輸入應產生相近 embedding。

**Acceptance Scenarios**:

1. **Given** 相同場景影像，**When** 生成 embedding，**Then** cosine similarity > 0.9。

---

### User Story 3 - VLM Prompt-Based Mapping (Priority: P3)

透過 VLM prompt 將觸感需求轉為視覺特徵搜尋。

**Why this priority**: 支援觸感對映是平台差異化特色。

**Independent Test**: 給定觸感描述，回傳合適物件候選。

**Acceptance Scenarios**:

1. **Given** "柔軟、球形" 觸感需求，**When** 查詢 VLM，**Then** 回傳 soft ball 類候選。

---

### Edge Cases

- 低光或模糊影像導致偵測率下降。
- VLM prompt 產生歧義結果。
- 模型推理延遲超出 SLA。

## Requirements *(mandatory)*

### Functional Requirements

- **AI-FR-001**: AI Layer MUST detect objects with bounding boxes and confidence scores.
- **AI-FR-002**: AI Layer MUST generate scene embeddings for Qdrant indexing.
- **AI-FR-003**: AI Layer MUST support VLM prompt-based search for tactile mapping.
- **AI-FR-004**: AI inference MUST return results within 1s for standard scan payloads.
- **AI-FR-005**: AI Layer MUST log model version and inference metadata.

### Key Entities *(include if feature involves data)*

- **DetectedObject**: label、bbox、confidence、features。
- **SceneEmbedding**: vector、source、timestamp。
- **PromptQuery**: tactile descriptor、response candidates。

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Object detection F1 ≥ 0.85 on curated dataset.
- **SC-002**: Scene embedding similarity score ≥ 0.9 for same scene.
- **SC-003**: VLM mapping precision ≥ 80% for tactile queries.
- **SC-004**: AI inference p95 latency < 1s for standard scans.
