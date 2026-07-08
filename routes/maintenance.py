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
from utils.pump_predictor import predict_pump
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
        pump_data = {}

        if request.form.get("category") == "Pump":

            pump_data = {

                "discharge_pressure": float(request.form.get("discharge_pressure") or 0),
                "discharge_flow": float(request.form.get("discharge_flow") or 0),

                "heater_pass1": float(request.form.get("heater_pass1") or 0),
                "heater_pass2": float(request.form.get("heater_pass2") or 0),
                "heater_pass3": float(request.form.get("heater_pass3") or 0),
                "heater_pass4": float(request.form.get("heater_pass4") or 0),

                "suction_temperature": float(request.form.get("suction_temperature") or 0),
                "suction_pressure": float(request.form.get("suction_pressure") or 0),

                "motor_nde_h": float(request.form.get("motor_nde_h") or 0),
                "motor_nde_pv": float(request.form.get("motor_nde_pv") or 0),
                "motor_nde_v": float(request.form.get("motor_nde_v") or 0),
                "motor_nde_a": float(request.form.get("motor_nde_a") or 0),

                "motor_de_h": float(request.form.get("motor_de_h") or 0),
                "motor_de_pv": float(request.form.get("motor_de_pv") or 0),
                "motor_de_v": float(request.form.get("motor_de_v") or 0),
                "motor_de_a": float(request.form.get("motor_de_a") or 0),

                "pump_de_h": float(request.form.get("pump_de_h") or 0),
                "pump_de_pv": float(request.form.get("pump_de_pv") or 0),
                "pump_de_v": float(request.form.get("pump_de_v") or 0),
                "pump_de_a": float(request.form.get("pump_de_a") or 0),

                "pump_nde_h": float(request.form.get("pump_nde_h") or 0),
                "pump_nde_pv": float(request.form.get("pump_nde_pv") or 0),
                "pump_nde_v": float(request.form.get("pump_nde_v") or 0),
                "pump_nde_a": float(request.form.get("pump_nde_a") or 0),
            }

            # Use representative values for the existing validation/report code
            temperature = pump_data["suction_temperature"]
            pressure = pump_data["discharge_pressure"]
            vibration = pump_data["pump_de_h"]

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

       # --------------------------------------------------
        # AI Prediction
        # --------------------------------------------------

        if equipment["category"] == "Pump":
            temperature = float(request.form.get("suction_temperature") or 0)

            pressure = float(request.form.get("discharge_pressure") or 0)

            vibration = float(request.form.get("pump_de_h") or 0)
            prediction_result = predict_pump(request.form)

        else:

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
            "pump_sensor_data": pump_data,

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
def get_equipment_summary():
    
    db = current_app.db

    records = list(db.maintenance_records.find())

    if not records:
        return {
            "health": 100,
            "flagged_assets": 0
        }

    total_health = 0
    flagged = 0

    for record in records:

        probability = record.get("failure_probability", 0)

        health = 100 - probability
        total_health += health

        if record.get("maintenance_required"):
            flagged += 1

    average_health = total_health / len(records)

    return {

        "health": round(average_health,1),

        "flagged_assets": flagged

    }