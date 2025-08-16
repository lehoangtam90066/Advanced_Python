from flask_sqlalchemy import SQLAlchemy
from application import app

db = SQLAlchemy(app)

# Định nghĩa mô hình (model) cho bảng User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
