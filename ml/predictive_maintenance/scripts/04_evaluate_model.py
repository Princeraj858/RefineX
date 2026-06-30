import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report
)
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_FOLDER = os.path.join(
    CURRENT_DIR,
    "..",
    "models"
)

PROCESSED_FOLDER = os.path.join(
    CURRENT_DIR,
    "..",
    "dataset",
    "processed"
)

REPORT_FOLDER = os.path.join(
    CURRENT_DIR,
    "..",
    "reports"
)

os.makedirs(REPORT_FOLDER, exist_ok=True)
model = joblib.load(

    os.path.join(
        MODEL_FOLDER,
        "refinery_model.pkl"
    )

)
test = pd.read_csv(

    os.path.join(
        PROCESSED_FOLDER,
        "test_dataset.csv"
    )

)

X_test = test.drop(
    columns=["Failure_Class"]
)

y_test = test["Failure_Class"]
predictions = model.predict(X_test)
accuracy = accuracy_score(
    y_test,
    predictions
)

precision = precision_score(
    y_test,
    predictions,
    average="weighted"
)

recall = recall_score(
    y_test,
    predictions,
    average="weighted"
)

f1 = f1_score(
    y_test,
    predictions,
    average="weighted"
)
print("="*60)
print("MODEL PERFORMANCE")
print("="*60)

print(f"Accuracy : {accuracy*100:.2f}%")
print(f"Precision: {precision*100:.2f}%")
print(f"Recall   : {recall*100:.2f}%")
print(f"F1 Score : {f1*100:.2f}%")
report = classification_report(
    y_test,
    predictions
)

print(report)

with open(

    os.path.join(
        REPORT_FOLDER,
        "classification_report.txt"
    ),

    "w"

) as file:

    file.write(report)

cm = confusion_matrix(
    y_test,
    predictions
)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm
)

disp.plot()

plt.title("Confusion Matrix")

plt.savefig(

    os.path.join(
        REPORT_FOLDER,
        "confusion_matrix.png"
    )

)

plt.show()
importance = pd.read_csv(

    os.path.join(
        REPORT_FOLDER,
        "feature_importance.csv"
    )

)

plt.figure(figsize=(8,5))

plt.bar(
    importance["Feature"],
    importance["Importance"]
)

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(

    os.path.join(
        REPORT_FOLDER,
        "feature_importance.png"
    )

)

plt.show()
