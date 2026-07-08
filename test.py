from ml.incident_management.predictor import predict_incident

text = """
Worker slipped from ladder while repairing pipeline valve.
"""

result = predict_incident(text)

print(result)