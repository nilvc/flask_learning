from flask import Flask
from db import db
import models
from authors.authors import authors_page
from users.users import users_page


if __name__ == "__main__":
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
    db.init_app(app)
    with app.app_context():
        db.create_all()

    app.register_blueprint(authors_page,url_prefix="/author")
    app.register_blueprint(users_page)
    app.run(debug=True)

