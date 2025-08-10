import click
from sqlalchemy.exc import SQLAlchemyError
from app.models import User, RoleEnum
from app.extensions import db


@click.command("create-admin")
@click.argument("username")
def create_admin(username):
    if User.query.filter_by(username=username).first():
        return print(f"User '{username}' already exists.")
    
    password = click.prompt("Password", hide_input=True, confirmation_prompt=True)

    email = click.prompt("E-mail", confirmation_prompt=True)

    new_admin = User(
        username=username,
        email=email,
        is_approved=True,
        role= RoleEnum.admin
    )

    new_admin.set_password(password)

    try:
        db.session.add(new_admin)
        db.session.commit()
        print(f"Admin user {username} successfully created!")
    
    except SQLAlchemyError as e:
        db.session.rollback() # "undo" for database
        print("Couldn't add new admin to database.")
        print(f"Database error: {e}")
