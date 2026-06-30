import os
import joblib
import pandas as pd

# ======================================================
# PATHS
# ======================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_DIR = os.path.join(
    BASE_DIR,
    "ml",
    "predictive_maintenance",
    "models"
)

# ======================================================
# LOAD MODEL & PREPROCESSORS
# ======================================================

model = joblib.load(
    os.path.join(MODEL_DIR, "refinery_model.pkl")
)

equipment_encoder = joblib.load(
    os.path.join(MODEL_DIR, "equipment_encoder.pkl")
)

label_encoder = joblib.load(
    os.path.join(MODEL_DIR, "label_encoder.pkl")
)

scaler = joblib.load(
    os.path.join(MODEL_DIR, "scaler.pkl")
)


# ======================================================
# PREDICTION FUNCTION
# ======================================================

def predict_equipment(
    equipment_type,
    temperature,
    pressure,
    vibration,
    operating_hours
):

    # Encode equipment type
    equipment = equipment_encoder.transform([equipment_type])[0]

    # Create DataFrame
    sample = pd.DataFrame({
        "Equipment_Type": [equipment],
        "Temperature": [float(temperature)],
        "Pressure": [float(pressure)],
        "Vibration": [float(vibration)],
        "Operating_Hours": [float(operating_hours)]
    })

    # Scale only sensor values
    sensor_columns = [
        "Temperature",
        "Pressure",
        "Vibration",
        "Operating_Hours"
    ]

    sample[sensor_columns] = scaler.transform(
        sample[sensor_columns]
    )

    # Prediction
    prediction_encoded = model.predict(sample)[0]

    prediction = label_encoder.inverse_transform(
        [prediction_encoded]
    )[0]

    # Probability
    probabilities = model.predict_proba(sample)[0]

    confidence = float(
        round(
            max(probabilities) * 100,
            2
        )
    )

    # Remaining Life & Recommendation
    if prediction == "Healthy":

        remaining_life = "180-365 Days"

        action = "Continue Normal Operation"

    elif prediction == "Warning":

        remaining_life = "60-180 Days"

        action = "Schedule Preventive Maintenance"

    elif prediction == "Critical":

        remaining_life = "7-30 Days"

        action = "Immediate Maintenance Required"

    else:

        remaining_life = "Immediate"

        action = "Shutdown Equipment Immediately"

    return {

        "prediction": prediction,

        "confidence": confidence,

        "remaining_life": remaining_life,

        "recommended_action": action,

        "failure_probability": float(
            round(
                100 - confidence,
                2
            )
        )
    }


# ======================================================
# TEST
# ======================================================

if __name__ == "__main__":

    result = predict_equipment(

        equipment_type="Pump",

        temperature=80,

        pressure=12,

        vibration=2,

        operating_hours=25000

    )

    print(result)