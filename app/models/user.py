
from app.extensions import db
class User(db.Model):
    __tablename__ = "user"
 
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer(),unique = True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.Integer())
    # position = db.Column(db.String(80))
 
    def __init__(self, user_id:int, first_name:str, last_name:str):
        self.employee_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        # self.position = position
 
    def __repr__(self):
        return f"{self.first_name} {self.last_name}:{self.user_id}"