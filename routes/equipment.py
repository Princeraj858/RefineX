from flask import Blueprint, request, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))

db = client["smart_refinery_ai"]

equipment_collection = db["equipment"]

equipment_bp = Blueprint("equipment", __name__)

# ==========================================================
# Equipment Autocomplete Search
# ==========================================================
@equipment_bp.route("/search-equipment", methods=["GET"])
def search_equipment():

    category = request.args.get("category", "").strip()
    query = request.args.get("query", "").strip()

    search = {}

    # Filter by category only if selected
    if category:
        search["category"] = category

    # Search by Equipment ID or Equipment Name
    if query:
        search["$or"] = [
            {
                "equipment_id": {
                    "$regex": query,
                    "$options": "i"
                }
            },
            {
                "equipment_name": {
                    "$regex": query,
                    "$options": "i"
                }
            }
        ]

    results = list(

        equipment_collection.find(

            search,

            {
                "_id": 0,
                "equipment_id": 1,
                "equipment_name": 1,
                "category": 1,
                "manufacturer": 1,
                "model": 1,
                "unit": 1,
                "section": 1,
                "health_index": 1,
                "status": 1
            }

        ).sort("equipment_id", 1).limit(10)

    )

    return jsonify({
        "success": True,
        "count": len(results),
        "equipment": results
    })


# ==========================================================
# Get Complete Equipment Details
# ==========================================================
@equipment_bp.route("/equipment/<equipment_id>", methods=["GET"])
def get_equipment(equipment_id):

    equipment = equipment_collection.find_one(

        {
            "equipment_id": equipment_id
        },

        {
            "_id": 0
        }

    )

    if equipment is None:

        return jsonify({
            "success": False,
            "message": "Equipment not found"
        }), 404

    return jsonify({
        "success": True,
        "equipment": equipment
    })

