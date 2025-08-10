from flask import abort
from flask_login import current_user
from app.models import RoleEnum
from functools import wraps


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not (current_user.is_authenticated) or not (current_user.role == RoleEnum.admin):
            return abort(403)
        return f(*args, **kwargs)
    return decorated_function