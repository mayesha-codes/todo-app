from app import db

class User(db.Model):
    user_id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(45),nullable=False)
    email=db.Column(db.String(45),unique=True,nullable=False)
    password=db.Column(db.String(45),nullable=False)
    role=db.Column(db.String(45),nullable=False)