from pydantic import BaseModel

class LegislatorDTO(BaseModel):
    id: int
    name: str

class LegislatorResponseDTO(LegislatorDTO):
    supported_bills: int
    opposed_bills: int
