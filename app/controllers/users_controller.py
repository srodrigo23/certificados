
from app.queries import users_queries


def get_all_users()->list:
    return users_queries.get_all_users()

def add_new_user(first_name:str, last_name:str, cell_phone:str)->bool:
    from app.models.user import User
    new_user = User(
        first_name=first_name,
        last_name=last_name,
        cell_phone=cell_phone,
    )
    return users_queries.insert_user(user=new_user)