from app import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

class Park(db.Model, UserMixin):
    __tablename__ = 'park'

    id = db.Column(db.Integer, primary_key=True)
    flour = db.Column(db.Integer, nullable=False)
    busy = db.Column(db.String(100), nullable=False)
    number = db.Column(db.String(100), nullable=True)

    def check_password(self, password: str):
        return self.number == password
