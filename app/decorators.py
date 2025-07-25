from flask import abort
from flask_login import current_user
from functools import wraps


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not (current_user.is_autheticated) or not (current_user.role == 'admin'):
            return abort(403)
        return f(*args, **kwargs)
    return decorated_function