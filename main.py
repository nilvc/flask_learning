from flask import Flask
from mongo_crud.authors_crud import author


if __name__ == "__main__":
    app = Flask(__name__)
    app.register_blueprint(author,url_prefix="/mongo_crud")
    app.run(debug=True)

