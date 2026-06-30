from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import create_access_token
from email_validator import validate_email, EmailNotValidError
from datetime import datetime
import re

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/signup", methods=["POST"])
def signup():

    try:

        data = request.get_json()

        name = data.get("name", "").strip()
        email = data.get("email", "").strip().lower()
        password = data.get("password", "").strip()
        address = data.get("address", "").strip()
        phone = data.get("phone", "").strip()

        if not all([name, email, password, address, phone]):

            return jsonify({
                "error": "All fields are required."
            }), 400

        if not re.match(r"^[A-Za-z\s]{3,30}$", name):

            return jsonify({
                "error": "Name should contain only letters and spaces."
            }), 400

        try:
            validate_email(email)

        except EmailNotValidError:

            return jsonify({
                "error": "Invalid email format."
            }), 400

        if not re.match(r"^[6-9]\d{9}$", phone):

            return jsonify({
                "error": "Enter valid 10-digit Indian mobile number."
            }), 400

        password_regex = (
            r"^(?=.*[a-z])"
            r"(?=.*[A-Z])"
            r"(?=.*\d)"
            r"(?=.*[@$!%*?&])"
            r"[A-Za-z\d@$!%*?&]{8,15}$"
        )

        if not re.match(password_regex, password):

            return jsonify({
                "error":
                "Password must contain uppercase, lowercase, digit, special character and be 8-15 characters long."
            }), 400

        db = current_app.db
        bcrypt = current_app.bcrypt

        users_collection = db["users"]

        existing_user = users_collection.find_one({
            "email": email
        })

        if existing_user:

            return jsonify({
                "error": "Email already registered."
            }), 409

        hashed_password = bcrypt.generate_password_hash(
            password
        ).decode("utf-8")

        new_user = {

            "name": name,
            "email": email,
            "password": hashed_password,
            "address": address,
            "phone": phone,
            "role": "farmer",
            "created_at": datetime.utcnow()
        }

        users_collection.insert_one(new_user)

        return jsonify({
            "message": "User registered successfully."
        }), 201

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500




@auth_bp.route("/login", methods=["POST"])
def login():

    try:

        data = request.get_json()

        email = data.get("email", "").strip().lower()
        password = data.get("password", "").strip()

        if not email or not password:

            return jsonify({
                "error": "Email and password are required."
            }), 400

        try:
            validate_email(email)

        except EmailNotValidError:

            return jsonify({
                "error": "Invalid email format."
            }), 400

        db = current_app.db
        bcrypt = current_app.bcrypt

        users_collection = db["users"]

        user = users_collection.find_one({
            "email": email
        })

        if not user:

            return jsonify({
                "error": "User not found."
            }), 404

        password_match = bcrypt.check_password_hash(
            user["password"],
            password
        )

        if not password_match:

            return jsonify({
                "error": "Incorrect password."
            }), 401

        access_token = create_access_token(
            identity=str(user["_id"])
        )

        return jsonify({

            "message": "Login successful.",

            "token": access_token,

            "user": {

                "name": user["name"],
                "email": user["email"],
                "role": user["role"]
            }

        }), 200

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500