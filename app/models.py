import enum
from app.extensions import db
from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class RoleEnum(enum.Enum):
    admin = "admin"
    user = "user"

class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    password_hash: Mapped[str]
    
    role: Mapped[RoleEnum] = mapped_column(Enum(RoleEnum, native_enum=False)) 
    # This tells SQLAlchemy not to use the database's specific ENUM type 
    # (which can be buggy or unsupported on some backends like SQLite) and 
    # instead create a standard VARCHAR column with a CHECK constraint. 
    # This approach works reliably across all database systems.

    is_approved: Mapped[bool] = mapped_column(default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
