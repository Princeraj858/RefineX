from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from pymongo import MongoClient
import os
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

# Import Blueprints
from routes.maintenance import maintenance_bp
from routes.equipment import equipment_bp
from routes.auth_routes import auth_bp
# Load environment variables
load_dotenv()

app = Flask(__name__)

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
# Run Application
if __name__ == "__main__":
    app.run(debug=True)