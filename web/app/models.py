from app import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

class Table1(db.Model, UserMixin):
    __tablename__ = 'table1'
    id = db.Column(db.Integer, primary_key=True)
    str1 = db.Column(db.String(100), nullable=False)
    str2 = db.Column(db.String(100), nullable=False)
    str3 = db.Column(db.String(100), nullable=False)


class Table2(db.Model, UserMixin):
    __tablename__ = 'table2'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    mesto = db.Column(db.String(100), nullable=False)

    def check_password(self, password: str):
        return self.password == password
