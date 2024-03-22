from flask import Blueprint, render_template
from src.modules.bill.bill_service import BillManagementService
from src.settings.adapters.base_adapter import BillDataAccess, LegislatorDataAccess, VoteDataAccess, VoteResultDataAccess
import json

bill_blueprint = Blueprint('bill_blueprint', __name__, template_folder='../../templates')

@bill_blueprint.route('')
def display_bills():
    billService = BillManagementService(BillDataAccess(), LegislatorDataAccess(), VoteDataAccess(), VoteResultDataAccess())
    allBills = billService.fetch_all_bills()
    chartInfo = {
        'labels': ['Supports', 'Oppositions'],
        'data': [sum(b.supporters for b in allBills), sum(b.opposers for b in allBills)],
    }
    chartDataStr = json.dumps(chartInfo, default=str)
    return render_template('bills.html', bills=allBills, chartData=chartDataStr)
