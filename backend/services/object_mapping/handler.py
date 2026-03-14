from backend.services.object_mapping.client import ObjectMappingClient
from backend.services.object_mapping.schemas import MappingRequest


def handle_mapping_request(payload: dict) -> dict:
    client = ObjectMappingClient()
    request = MappingRequest(**payload)
    response = client.request_mapping(request)
    return response.model_dump()
