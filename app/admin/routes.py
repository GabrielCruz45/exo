# Route for the user approval dashboard
from flask import Blueprint, abort
from flask_login import login_required

from ..decorators import admin_required


admin_bp = Blueprint(
    'admin',
    __name__,
    template_folder='templates/admin',
    url_prefix='/admin'
)



@admin_bp.route('/dashboard')
@login_required
@admin_required
def admin_dashboard():
    return