from pydantic import BaseModel

class VoteDTO(BaseModel):
    id: int
    bill_id: int
