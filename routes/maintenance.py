from flask import (
    Blueprint,
    render_template,
    request,
    jsonify,
    current_app
)
from uuid import uuid4
from werkzeug.utils import secure_filename
from utils.predictor import predict_equipment
import os
from datetime import datetime

maintenance_bp = Blueprint("maintenance", __name__)

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ==========================================================
# Home
# ==========================================================

@maintenance_bp.route("/")
def home():
    return render_template("equipment.html")


# ==========================================================
# Predict Maintenance
# ==========================================================

@maintenance_bp.route("/predict", methods=["POST"])
def predict():

    try:

        db = current_app.db

        equipment_collection = db["equipment"]

        maintenance_collection = db["maintenance_records"]

        # --------------------------------------------------
        # Form Data
        # --------------------------------------------------

        equipment_id = request.form.get("equipment_id")

        temperature = float(request.form.get("temperature") or 0)

        pressure = float(request.form.get("pressure") or 0)

        vibration = float(request.form.get("vibration") or 0)

        operating_hours = int(request.form.get("hours") or 0)

        image = request.files.get("image")

        # --------------------------------------------------
        # Equipment Lookup
        # --------------------------------------------------

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

                "message": "Equipment not found."

            }),404
        # --------------------------------------------------
        # Engineering Limit Validation
        # --------------------------------------------------

        sensor_status = {}

        # Temperature
        if equipment["alarm_temperature"] is not None:

            if temperature >= equipment["alarm_temperature"]:

                sensor_status["temperature"] = "CRITICAL"

            elif temperature >= equipment["warning_temperature"]:

                sensor_status["temperature"] = "WARNING"

            else:

                sensor_status["temperature"] = "NORMAL"

        else:

            sensor_status["temperature"] = "N/A"


        # Pressure
        if equipment["alarm_pressure"] is not None:

            if pressure >= equipment["alarm_pressure"]:

                sensor_status["pressure"] = "CRITICAL"

            elif pressure >= equipment["warning_pressure"]:

                sensor_status["pressure"] = "WARNING"

            else:

                sensor_status["pressure"] = "NORMAL"

        else:

            sensor_status["pressure"] = "N/A"


        # Vibration
        if equipment["alarm_vibration"] is not None:

            if vibration >= equipment["alarm_vibration"]:

                sensor_status["vibration"] = "CRITICAL"

            elif vibration >= equipment["warning_vibration"]:

                sensor_status["vibration"] = "WARNING"

            else:

                sensor_status["vibration"] = "NORMAL"

        else:

            sensor_status["vibration"] = "N/A"
        

        # --------------------------------------------------
        # Save Image
        # --------------------------------------------------

        image_path = ""

        if image and image.filename:

            filename = f"{uuid4()}_{secure_filename(image.filename)}"

            image_path = os.path.join(

                UPLOAD_FOLDER,

                filename

            )

            image.save(image_path)

       # --------------------------------------------------
        # AI Prediction
        # --------------------------------------------------

        prediction_result = predict_equipment(

            equipment_type=equipment["category"],

            temperature=temperature,

            pressure=pressure,

            vibration=vibration,

            operating_hours=operating_hours

        )

        prediction = prediction_result["prediction"]

        confidence = prediction_result["confidence"]

        remaining_life = prediction_result["remaining_life"]

        action = prediction_result["recommended_action"]

        failure_probability = prediction_result["failure_probability"]

        # --------------------------------------------------
        # Store Maintenance Record
        # --------------------------------------------------

        maintenance_collection.insert_one({

            "equipment_id": equipment["equipment_id"],

            "equipment_name": equipment["equipment_name"],

            "category": equipment["category"],

            "manufacturer": equipment["manufacturer"],

            "model": equipment["model"],

            "unit": equipment["unit"],

            "section": equipment["section"],

            "temperature": temperature,

            "pressure": pressure,

            "vibration": vibration,
            "sensor_status": sensor_status,

            "operating_hours": operating_hours,

            "image_path": image_path,

            "prediction": prediction,

            "confidence": confidence,

            "remaining_life": remaining_life,

            "recommended_action": action,

            "failure_probability": failure_probability,

            "predicted_failure": prediction,

            "maintenance_required": prediction != "Healthy",

            "model_version": "RandomForest_v2",

            "created_at": datetime.utcnow()

        })

        # --------------------------------------------------
        # Response
        # --------------------------------------------------
        overall_status = "Healthy"

        if "CRITICAL" in sensor_status.values():

            overall_status = "Critical"

        elif "WARNING" in sensor_status.values():

             overall_status = "Monitor"
        return jsonify({

        "success": True,

        "prediction": prediction,

        "confidence": confidence,

        "remaining_life": remaining_life,

        "action": action,

        "failure_probability": failure_probability,

        "overall_status": overall_status,

        "sensor_status": sensor_status

    })

    except Exception as e:

        return jsonify({

            "success": False,

            "error": str(e)

        }),500