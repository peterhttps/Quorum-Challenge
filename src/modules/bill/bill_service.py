from src.settings.DTOs.bill_dto import BillDTO, BillResponseDTO
from src.settings.DTOs.legislator_dto import LegislatorDTO
from src.settings.DTOs.vote_dto import VoteDTO
from src.settings.DTOs.vote_result_dto import VoteResultDTO

class BillManagementService:
    def __init__(self, billSrc, legislatorSrc, voteSrc, voteResultSrc):
        self.billSrc = billSrc
        self.legislatorSrc = legislatorSrc
        self.voteSrc = voteSrc
        self.voteResultSrc = voteResultSrc

    def fetch_all_bills(self):
        billData = self.billSrc.fetch_data()
        voteResults = self.voteResultSrc.fetch_data()
        billDetails = []

        for bill in billData:
            billVotes = [vote for vote in self.voteSrc.fetch_data() if vote.bill_id == bill.id]
            voteResultsForBill = [vResult for vResult in voteResults for vote in billVotes if vResult.vote_id == vote.id]

            billSupports = sum(1 for vResult in voteResultsForBill if vResult.vote_type == 1)
            billOpposes = sum(1 for vResult in voteResultsForBill if vResult.vote_type != 1)

            primarySponsorName = next((legislator.name for legislator in self.legislatorSrc.fetch_data() if legislator.id == bill.sponsor_id), "Anonymous")


            billDetails.append(
                BillResponseDTO(
                    id=bill.id, 
                    title=bill.title, 
                    supporters=billSupports, 
                    opposers=billOpposes, 
                    primary_sponsor=primarySponsorName
                )
            )


        return billDetails
