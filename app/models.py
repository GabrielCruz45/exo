import enum
from .models import db
from typing import List
from sqlalchemy import ForeignKey, String, Enum, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import func

class RoleEnum(enum.Enum):
    admin = "admin"
    user = "user"

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    password_hash: Mapped[str]
    
    role: Mapped[RoleEnum] = mapped_column(Enum(RoleEnum, native_enum=False)) # This tells SQLAlchemy not to use the database's specific ENUM type (which can be buggy or unsupported on some backends like SQLite) and instead create a standard VARCHAR column with a CHECK constraint. This approach works reliably across all database systems.
    # some_user = User(role=RoleEnum.admin)
    # another_user = User(role=RoleEnum.user)

    is_approved: Mapped[bool] = mapped_column(default=False)
