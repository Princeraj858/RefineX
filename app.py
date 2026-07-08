from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from pymongo import MongoClient
import os
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask import Flask, jsonify, render_template,send_from_directory
import joblib
from ml.production_forecasting.pf.api.app import forecast_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
# Import Blueprints
from routes.maintenance import maintenance_bp,get_equipment_summary
from routes.equipment import equipment_bp
from routes.auth_routes import auth_bp
from routes.contact import contact_bp
from routes.reports import reports_bp
from routes.incident_routes import incident_bp,get_safety_summary
from routes.innovation import innovation_bp
from ml.production_forecasting.pf.api.app import get_production_summary,get_efficiency
# Load environment variables
load_dotenv()

app = Flask(__name__)
app.wsgi_app = DispatcherMiddleware(
    app.wsgi_app,
    {
        "/production": forecast_app
    }
)
# Enable CORS
CORS(app)
bcrypt = Bcrypt(app)

jwt = JWTManager(app)
app.bcrypt = bcrypt
# Secret Key
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

# Upload folder
app.config["UPLOAD_FOLDER"] = "uploads"

# MongoDB Connection
client = MongoClient(os.getenv("MONGO_URI"))

try:
    client.admin.command("ping")
    print("✅ MongoDB Connected")
except Exception as e:
    print("❌ MongoDB Connection Failed")
    print(e)
    exit()

db = client["smart_refinery_ai"]
app.db = db

# Register Routes
app.register_blueprint(maintenance_bp)
app.register_blueprint(equipment_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(contact_bp)
app.register_blueprint(reports_bp)
app.register_blueprint(incident_bp)
app.register_blueprint(innovation_bp, url_prefix="/api")
def uploaded_file(filename):
    return send_from_directory("uploads", filename)

@app.route("/api/home-dashboard")
def home_dashboard():

    prod = get_production_summary()
    eff = get_efficiency()
    equip = get_equipment_summary()
    safe = get_safety_summary()

    return jsonify({

        "production_today": prod["production_today"],
        "production_change": prod["change"],

        "plant_efficiency": eff["efficiency"],
        "efficiency_change": eff["change"],

        "safety_index": safe["safety_index"],
        "safety_change": safe["safety_change"],

        "equipment_health": equip["health"],
        "flagged_assets": equip["flagged_assets"]

    })
# Run Application
if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
)