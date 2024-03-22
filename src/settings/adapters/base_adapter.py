import csv

from pydantic import BaseModel

from src.settings.DTOs.legislator_dto import LegislatorDTO
from src.settings.DTOs.bill_dto import BillDTO
from src.settings.DTOs.vote_dto import VoteDTO
from src.settings.DTOs.vote_result_dto import VoteResultDTO

class BaseAdapter:
    path: str
    dto: BaseModel

    def fetch_data(self):
        with open(self.path, 'r') as file:
            reader = csv.DictReader(file)
            return [self.dto(**row) for row in reader]

class BillDataAccess(BaseAdapter):
    path = ("data/bills_(2).csv")
    dto = BillDTO

class LegislatorDataAccess(BaseAdapter):
    path = ("data/legislators_(2).csv")
    dto = LegislatorDTO

class VoteDataAccess(BaseAdapter):
    path = ("data/votes_(2).csv")
    dto = VoteDTO

class VoteResultDataAccess(BaseAdapter):
    path = ("data/vote_results_(2).csv")
    dto = VoteResultDTO
