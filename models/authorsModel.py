from db import db

class Authors(db.Model):
    __tablename__ = "Authors"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Integer,unique=True,nullable=False)

    def __str__(self):
        return "id - {} , name - {}".format(self.id,self.name)

