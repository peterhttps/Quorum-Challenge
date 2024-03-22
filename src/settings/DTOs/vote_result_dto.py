from pydantic import BaseModel

class VoteResultDTO(BaseModel):
    id: int
    legislator_id: int
    vote_id: int
    vote_type: int
