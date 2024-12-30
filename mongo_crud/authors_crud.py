from flask import request,Blueprint
from pymongo import MongoClient

author = Blueprint("author",__name__)

def getMongoClient():
	# Set up MongoDB connection
	client = MongoClient('mongodb://localhost:27017/')
	db = client['flask_learning']
	return db


@author.post('/add_author')
def add_author():
	# Get data from request
	data = request.json
	print(data)
	# Insert data into MongoDB
	db = getMongoClient()
	collection = db["authors"]
	collection.insert_one(data)

	return 'Data added to MongoDB'

@author.get("/author/<int:id>")
def get_author(id):
	db = getMongoClient()
	users=db.authors.find({"_id":id})
	return {
	"data": list(users)
	}, 200


@author.delete("/author/<int:id>")
def delete_author(id):
	db = getMongoClient()
	query = {"_id": id}
	result = db.authors.delete_one(query)
	if not result.deleted_count:
		return {"message": "Failed to delete"}, 500

	return {"message": "Delete success"}, 200


@author.put("/author/<int:id>")
def update_user(id):
	db = getMongoClient()
	query = {"_id": id}
	content = {"$set": dict(request.json)}
	result = db.authors.update_one(query, content)

	if not result.matched_count:
		return {"message": "Failed to update. Record is not found" }, 404

	if not result.modified_count:
		return {"message": "No changes applied"}, 500

	return {"message": "Update success"}, 200