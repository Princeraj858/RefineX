from flask import Blueprint, request, jsonify, current_app
from bson import ObjectId
from pymongo import DESCENDING

innovation_bp = Blueprint("innovation", __name__)


def get_collection():
    return current_app.db["innovation_ideas"]
@innovation_bp.route("/ideas", methods=["POST"])
def add_idea():
    collection = get_collection()

    data = request.json

    idea = {
    "title": data.get("title"),
    "description": data.get("description"),
    "category": data.get("category"),
    "author": data.get("author"),
    "department": "IOCL Guwahati",
    "likes": 0,
    "comments": 0,
    "status": "Active"
}
    result = collection.insert_one(idea)

    return jsonify({
        "success": True,
        "message": "Idea submitted successfully",
        "id": str(result.inserted_id)
    }), 201
@innovation_bp.route("/ideas", methods=["GET"])
def get_ideas():
    collection = get_collection()

    ideas = []

    for idea in collection.find().sort("_id", DESCENDING):
        idea["_id"] = str(idea["_id"])
        ideas.append(idea)

    return jsonify(ideas), 200
