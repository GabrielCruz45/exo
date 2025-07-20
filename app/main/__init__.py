# /main Blueprint definition
from flask import Blueprint

homepage_bp = Blueprint('homepage', __name__)

# The reason it goes at the bottom is to avoid a circular import. 
# You must define bp before you import the routes file that depends on bp.
from . import routes