from flask import Blueprint, request, jsonify, current_app
from bson import ObjectId
from math import ceil
from pymongo import DESCENDING, ASCENDING

reports_bp = Blueprint("reports", __name__)
def get_collection():

    return current_app.db["maintenance_records"]
@reports_bp.route("/api/reports/stats", methods=["GET"])
def report_stats():

    collection = get_collection()

    total = collection.count_documents({})

    healthy = collection.count_documents({
        "prediction": "Healthy"
    })

    warning = collection.count_documents({
        "prediction": "Warning"
    })

    critical = collection.count_documents({
        "prediction": "Critical"
    })

    return jsonify({

        "total": total,

        "healthy": healthy,

        "warning": warning,

        "critical": critical

    })
@reports_bp.route("/api/reports", methods=["GET"])
def get_reports():
    page = int(request.args.get("page",1))

    limit = int(request.args.get("limit",10))

    status = request.args.get("status","")

    category = request.args.get("category","")

    search = request.args.get("search","")

    sort = request.args.get("sort","newest")
    query = {}
    if status:

        query["prediction"] = status
    if category:

        query["category"] = category
    if search:

        query["$or"] = [

            {

                "equipment_name":{

                    "$regex":search,

                    "$options":"i"

                }

            },

            {

                "equipment_id":{

                    "$regex":search,

                    "$options":"i"

                }

            }

        ]
    sort_order = DESCENDING
    if sort == "oldest":

        sort_order = ASCENDING
    collection = get_collection()

    total = collection.count_documents(query)

    pages = ceil(total/limit)
    cursor = (

        collection

        .find(query)

        .sort("created_at",sort_order)

        .skip((page-1)*limit)

        .limit(limit)

    )
    reports = []
    for report in cursor:

        report["_id"] = str(report["_id"])

        reports.append(report)
    return jsonify({

        "page":page,

        "pages":pages,

        "total":total,

        "reports":reports

    })
@reports_bp.route("/api/reports/<report_id>", methods=["GET"])
def get_single_report(report_id):

    collection = get_collection()

    report = collection.find_one({

        "_id":ObjectId(report_id)

    })

    if not report:

        return jsonify({

            "error":"Report not found"

        }),404

    report["_id"] = str(report["_id"])

    return jsonify(report)
@reports_bp.route("/api/reports/categories", methods=["GET"])
def get_categories():

    collection = get_collection()

    categories = collection.distinct("category")

    categories.sort()

    return jsonify(categories)
