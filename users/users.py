from flask import Blueprint


users_page = Blueprint('user_page', __name__)

@users_page.route('/',methods=["GET"])
def show():
    return "<h1> Hello from users <h1>"

@users_page.route('/name',methods=["GET"])
def showName():
    return "<h1> Hello from users with name <h1>"