import os
import joblib
import pandas as pd

# ==========================================================
# Load Model
# ==========================================================

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

MODEL_DIR = os.path.join(BASE_DIR, "ml", "models")

model = joblib.load(os.path.join(MODEL_DIR, "predictive_model.pkl"))
scaler = joblib.load(os.path.join(MODEL_DIR, "scaler.pkl"))
encoder = joblib.load(os.path.join(MODEL_DIR, "label_encoder.pkl"))

# ==========================================================
# Pump Prediction
# ==========================================================

def predict_pump(form):

    # -----------------------------
    # Read Original Sensor Values
    # -----------------------------

    data = {

        "Discharge_Pressure": float(form.get("discharge_pressure", 0)),
        "Discharge_Flow": float(form.get("discharge_flow", 0)),

        "Heater_Pass1": float(form.get("heater_pass1", 0)),
        "Heater_Pass2": float(form.get("heater_pass2", 0)),
        "Heater_Pass3": float(form.get("heater_pass3", 0)),
        "Heater_Pass4": float(form.get("heater_pass4", 0)),

        "Suction_Temperature": float(form.get("suction_temperature", 0)),
        "Suction_Pressure": float(form.get("suction_pressure", 0)),

        "Motor_NDE_H": float(form.get("motor_nde_h", 0)),
        "Motor_NDE_PV": float(form.get("motor_nde_pv", 0)),
        "Motor_NDE_V": float(form.get("motor_nde_v", 0)),
        "Motor_NDE_A": float(form.get("motor_nde_a", 0)),

        "Motor_DE_H": float(form.get("motor_de_h", 0)),
        "Motor_DE_PV": float(form.get("motor_de_pv", 0)),
        "Motor_DE_V": float(form.get("motor_de_v", 0)),
        "Motor_DE_A": float(form.get("motor_de_a", 0)),

        "Pump_DE_H": float(form.get("pump_de_h", 0)),
        "Pump_DE_PV": float(form.get("pump_de_pv", 0)),
        "Pump_DE_V": float(form.get("pump_de_v", 0)),
        "Pump_DE_A": float(form.get("pump_de_a", 0)),

        "Pump_NDE_H": float(form.get("pump_nde_h", 0)),
        "Pump_NDE_PV": float(form.get("pump_nde_pv", 0)),
        "Pump_NDE_V": float(form.get("pump_nde_v", 0)),
        "Pump_NDE_A": float(form.get("pump_nde_a", 0))
    }

    # -----------------------------
    # Feature Engineering
    # -----------------------------

    data["Avg_Heater_Flow"] = (
        data["Heater_Pass1"] +
        data["Heater_Pass2"] +
        data["Heater_Pass3"] +
        data["Heater_Pass4"]
    ) / 4

    data["Motor_Vibration"] = (
        data["Motor_NDE_H"] +
        data["Motor_DE_H"]
    ) / 2

    data["Pump_Vibration"] = (
        data["Pump_DE_H"] +
        data["Pump_NDE_H"]
    ) / 2

    data["Overall_Vibration"] = (
        data["Motor_NDE_H"] +
        data["Motor_DE_H"] +
        data["Pump_DE_H"] +
        data["Pump_NDE_H"]
    ) / 4

    data["Pressure_Flow_Index"] = (
        data["Discharge_Pressure"] *
        data["Discharge_Flow"]
    )

    # NOTE:
    # During training this used the dataset mean.
    # For a single prediction we approximate deviation from nominal.
    # If you saved the training mean, use that instead.
    NOMINAL_SUCTION_TEMP = 357.0
    data["Temp_Deviation"] = abs(
        data["Suction_Temperature"] -
        NOMINAL_SUCTION_TEMP
    )

    # -----------------------------
    # Feature Order
    # -----------------------------

    feature_order = [

        "Discharge_Pressure",
        "Discharge_Flow",

        "Heater_Pass1",
        "Heater_Pass2",
        "Heater_Pass3",
        "Heater_Pass4",

        "Suction_Temperature",
        "Suction_Pressure",

        "Motor_NDE_H",
        "Motor_NDE_PV",
        "Motor_NDE_V",
        "Motor_NDE_A",

        "Motor_DE_H",
        "Motor_DE_PV",
        "Motor_DE_V",
        "Motor_DE_A",

        "Pump_DE_H",
        "Pump_DE_PV",
        "Pump_DE_V",
        "Pump_DE_A",

        "Pump_NDE_H",
        "Pump_NDE_PV",
        "Pump_NDE_V",
        "Pump_NDE_A",

        "Avg_Heater_Flow",
        "Motor_Vibration",
        "Pump_Vibration",
        "Overall_Vibration",
        "Pressure_Flow_Index",
        "Temp_Deviation"
    ]

    df = pd.DataFrame([[data[col] for col in feature_order]],
                      columns=feature_order)

    scaled = scaler.transform(df)

    prediction = model.predict(scaled)[0]

    probabilities = model.predict_proba(scaled)[0]

    health = encoder.inverse_transform([prediction])[0]

    confidence = round(max(probabilities) * 100, 2)

    # -----------------------------
    # Business Logic
    # -----------------------------

    if health == "Healthy":

        failure_probability = 10
        remaining_life = 300
        recommended_action = "Routine Inspection"

    elif health == "Warning":

        failure_probability = 45
        remaining_life = 150
        recommended_action = "Schedule Maintenance"

    else:

        failure_probability = 85
        remaining_life = 30
        recommended_action = "Immediate Maintenance"

    return {

        "prediction": health,

        "confidence": confidence,

        "remaining_life": remaining_life,

        "recommended_action": recommended_action,

        "failure_probability": failure_probability
    }