from db import db


class Posts(db.Model):
    __tablename__ = "Posts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, unique=True, nullable=False)

