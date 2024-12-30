from flask import Blueprint
from flask import request
from db import db
from models.authorsModel import Authors


authors_page = Blueprint('author_page', __name__)

@authors_page.route('/',methods=["GET"])
def show():
    return "<h1> Hello from authors <h1>"

@authors_page.route('/name',methods=["GET"])
def showName(name):
    return f"<h1> Hello from authors to escape {name} <h1>"

@authors_page.post('/create')
def createAuthor():
    data  = request.get_json()
    id = data.get("id","")
    name = data.get("name","")
    author = Authors(id=id,name=name)
    db.session.add(author)
    db.session.commit()
    print(author)
    return "debuging"

@authors_page.get("/getAuthor/<id>")
def getAuthor(id):
    print("Getting author with id - {}".format(id))
    author = Authors.query.get_or_404(id)
    return str(author)




@authors_page.errorhandler(404)
def page_not_found(e):
    return "<h3>Not sure what you need<h3>"