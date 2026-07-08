import os
import joblib

from .preprocessing import clean_text

# Current folder
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Model folder
MODEL_DIR = os.path.join(CURRENT_DIR, "models")

# Load model files once
model = joblib.load(
    os.path.join(MODEL_DIR, "best_incident_model.pkl")
)

vectorizer = joblib.load(
    os.path.join(MODEL_DIR, "tfidf_vectorizer.pkl")
)

label_encoder = joblib.load(
    os.path.join(MODEL_DIR, "label_encoder.pkl")
)


def predict_incident(text):
    """
    Predict incident severity from raw incident text.
    """

    if not text or not text.strip():
        return {
            "success": False,
            "message": "Incident description cannot be empty."
        }

    # Clean text
    cleaned_text = clean_text(text)

    # TF-IDF
    vector = vectorizer.transform([cleaned_text])

    # Prediction
    prediction = model.predict(vector)

    severity = label_encoder.inverse_transform(prediction)[0]

    return {
        "success": True,
        "incident": text,
        "clean_text": cleaned_text,
        "severity": severity,
        "model": "Linear SVM"
    }