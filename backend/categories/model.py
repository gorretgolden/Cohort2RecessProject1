from backend.db import db
from dataclasses import dataclass

@dataclass
class Category(db.Model):
    __tablename__ = "categories"
    name:str
    image:str
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255),unique=True)
    image = db.Column(db.String(255),nullable=False)
    created_by  = db.Column(db.Integer,db.ForeignKey('users.id'))
    created_at = db.Column(db.String(255),nullable=True)
    updated_at = db.Column(db.String(255),nullable=True)
    
   

    def __init__(self, image, name,created_by,created_at,updated_at):
     self.image = image
     self.name = name
     self.created_by = created_by
     self.created_at = created_at
     self.updated_at = updated_at
    

    def __repr__(self):
        return f"<Category {self.name} >"
