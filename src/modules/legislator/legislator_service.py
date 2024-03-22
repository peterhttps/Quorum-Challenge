from src.settings.DTOs.legislator_dto import LegislatorDTO, LegislatorResponseDTO
from src.settings.DTOs.vote_result_dto import VoteResultDTO
from src.settings.adapters.base_adapter import LegislatorDataAccess, VoteResultDataAccess

class LegislatorManagementService:
    def __init__(self, legislator_source: LegislatorDataAccess, vote_results_source: VoteResultDataAccess):
        self.legislator_source = legislator_source
        self.vote_results_source = vote_results_source

    def get_legislators_info(self) -> list[LegislatorResponseDTO]:
        all_legislators = self.legislator_source.fetch_data()
        all_vote_results = self.vote_results_source.fetch_data()
        legislators_info = []

        for legislator in all_legislators:
            votes = [vote for vote in all_vote_results if vote.legislator_id == legislator.id]
            supported = sum(vote.vote_type == 1 for vote in votes)
            opposed = len(votes) - supported

            legislators_info.append(
                LegislatorResponseDTO(
                    id=legislator.id,
                    name=legislator.name,
                    supported_bills=supported,
                    opposed_bills=opposed,
                )
            )

        return legislators_info