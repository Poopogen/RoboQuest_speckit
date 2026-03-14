from backend.services.object_mapping.schemas import MappingRequest, MappingResponse


class ObjectMappingClient:
    def request_mapping(self, payload: MappingRequest) -> MappingResponse:
        return MappingResponse(mapping_id="pending", status="queued", estimated_latency_ms=800)
