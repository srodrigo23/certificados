
from app.models.user import User

def get_all_users()->list:
    return User.query.all()

def insert_user(user: User)->bool:
    User.insert(user)
    return True