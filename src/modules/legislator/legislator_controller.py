from flask import Blueprint, render_template
from src.modules.legislator.legislator_service import LegislatorManagementService
from src.settings.adapters.base_adapter import LegislatorDataAccess, VoteResultDataAccess

legislator_blueprint = Blueprint('legislators', __name__, template_folder='../../templates')

@legislator_blueprint.route('')
def display_legislators():
    manager = LegislatorManagementService(LegislatorDataAccess(), VoteResultDataAccess())
    legislators_list = manager.get_legislators_info()
    chart_info = {
        'labels': ['Supported Bills', 'Opposed Bills'],
        'data': [
            sum(leg.supported_bills for leg in legislators_list),
            sum(leg.opposed_bills for leg in legislators_list),
        ],
    }
    return render_template('legislators.html', legislators=legislators_list, chart_data=chart_info)
