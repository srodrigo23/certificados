
from app.extensions import db
from app.models.base import Base
class User(Base):
    __tablename__ = "Users"
 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # user_id = db.Column(db.Integer(), unique = True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.Integer())
    cell_phone = db.Column(db.String(12))

    def __init__(self, first_name:str, last_name:str, cell_phone:str):
        self.first_name = first_name
        self.last_name = last_name
        self.cell_phone = cell_phone
 
    def __repr__(self):
        return f"{self.first_name} {self.last_name} : {self.id} : {self.date_created}"