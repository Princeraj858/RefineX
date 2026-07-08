from flask import Blueprint, request, jsonify
from flask import current_app
from datetime import datetime
from ml.incident_management.predictor import predict_incident

incident_bp = Blueprint("incident", __name__)


@incident_bp.route("/predict_incident", methods=["POST"])
def predict():

    try:

        data = request.get_json(silent=True) or {}

        incident_text = data.get("incident", "").strip()

        result = predict_incident(incident_text)

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500
@incident_bp.route("/test_prediction")
def test_prediction():

    result = predict_incident(
        "Worker slipped from ladder while repairing pipeline valve."
    )

    return jsonify(result)
@incident_bp.route("/submit_incident", methods=["POST"])
def submit_incident():

    try:

        data = request.get_json()

        db = current_app.db

        total = db.incidents.count_documents({}) + 1

        incident_id = f"INC-{datetime.now().year}-{total:04d}"

        incident = {

            "incident_id": incident_id,

            "title": data.get("title"),

            "department": data.get("department"),

            "location": data.get("location"),

            "description": data.get("description"),

            "severity": data.get("severity"),

            "model": data.get("model"),

            "status": "Open",

            "created_at": datetime.utcnow(),
            "ai_completed": True
        }

        db.incidents.insert_one(incident)

        return jsonify({

            "success": True,

            "incident_id": incident_id

        })

    except Exception as e:

        print(e)

        return jsonify({

            "success": False,

            "message": "Unable to save incident."

        }),500
@incident_bp.route("/incident_stats")
def incident_stats():

    db = current_app.db

    open_count = db.incidents.count_documents({
        "status":"Open"
    })

    resolved = db.incidents.count_documents({
        "status":"Resolved"
    })

    investigating = db.incidents.count_documents({
        "status":"Investigating"
    })

    total = db.incidents.count_documents({})

    return jsonify({

        "open":open_count,

        "resolved":resolved,

        "investigating":investigating,

        "total":total

    })
@incident_bp.route("/recent_incidents")
def recent_incidents():

    db = current_app.db

    page = int(request.args.get("page", 1))
    limit = 6

    skip = (page - 1) * limit

    total = db.incidents.count_documents({})

    cursor = (
        db.incidents
        .find()
        .sort("created_at", -1)
        .skip(skip)
        .limit(limit)
    )

    incidents = []

    for item in cursor:

        incidents.append({

            "id": item["incident_id"],
            "title": item["title"],
            "department": item["department"],
            "severity": item.get("severity", "Unknown"),
            "status": item["status"],
            "date": item["created_at"].strftime("%d %b %Y")

        })

    return jsonify({

        "incidents": incidents,

        "page": page,

        "limit": limit,

        "total": total

    })
@incident_bp.route("/update_incident_status", methods=["PUT"])
def update_incident_status():

    try:

        data = request.get_json()

        db = current_app.db

        result = db.incidents.update_one(

            {
                "incident_id": data["incident_id"]
            },

            {
                "$set":{
                    "status":data["status"]
                }
            }

        )

        return jsonify({

            "success":result.modified_count>0

        })

    except Exception as e:

        print(e)

        return jsonify({

            "success":False

        }),500
@incident_bp.route("/incident/<incident_id>")
def get_incident(incident_id):

    db = current_app.db

    incident = db.incidents.find_one(
        {"incident_id": incident_id},
        {"_id": 0}
    )

    if not incident:
        return jsonify({
            "success": False,
            "message": "Incident not found."
        }),404

    incident["created_at"] = incident["created_at"].strftime(
        "%d %b %Y %I:%M %p"
    )

    return jsonify({
        "success": True,
        "incident": incident
    })
def get_safety_summary():

    db = current_app.db

    total = db.incidents.count_documents({})

    if total == 0:

        return {

            "safety_index":100,

            "change":0

        }

    critical = db.incidents.count_documents({
        "severity":"Critical"
    })

    high = db.incidents.count_documents({
        "severity":"High"
    })

    medium = db.incidents.count_documents({
        "severity":"Medium"
    })

    low = db.incidents.count_documents({
        "severity":"Low"
    })

    penalty = (

        critical*10 +

        high*6 +

        medium*3 +

        low

    )

    safety_index = max(

        0,

        100-(penalty/total)

    )

    return {

        "safety_index":round(safety_index,1),

        "safety_change":0

    }