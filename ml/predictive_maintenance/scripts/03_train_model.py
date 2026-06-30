import os
import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

PROCESSED_FOLDER = os.path.join(
    CURRENT_DIR,
    "..",
    "dataset",
    "processed"
)

MODEL_FOLDER = os.path.join(
    CURRENT_DIR,
    "..",
    "models"
)

REPORT_FOLDER = os.path.join(
    CURRENT_DIR,
    "..",
    "reports"
)

os.makedirs(REPORT_FOLDER, exist_ok=True)
print("=" * 60)
print("LOADING TRAINING DATA")
print("=" * 60)

train = pd.read_csv(
    os.path.join(
        PROCESSED_FOLDER,
        "train_dataset.csv"
    )
)

test = pd.read_csv(
    os.path.join(
        PROCESSED_FOLDER,
        "test_dataset.csv"
    )
)
X_train = train.drop(
    columns=["Failure_Class"]
)

y_train = train["Failure_Class"]

X_test = test.drop(
    columns=["Failure_Class"]
)

y_test = test["Failure_Class"]
model = RandomForestClassifier(

    n_estimators=300,

    max_depth=20,

    min_samples_split=5,

    min_samples_leaf=2,

    random_state=42,

    n_jobs=-1

)
print("\nTraining Random Forest...\n")

model.fit(
    X_train,
    y_train
)

print("Training Completed.")
predictions = model.predict(
    X_test
)
accuracy = accuracy_score(
    y_test,
    predictions
)

print("\nAccuracy")

print(round(
    accuracy * 100,
    2
), "%")

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

print("\nConfusion Matrix\n")

print(cm)
joblib.dump(

    model,

    os.path.join(

        MODEL_FOLDER,

        "refinery_model.pkl"

    )

)

print("\nModel Saved Successfully.")
importance = pd.DataFrame({

    "Feature": X_train.columns,

    "Importance": model.feature_importances_

})

importance = importance.sort_values(

    by="Importance",

    ascending=False

)

print("\nFeature Importance\n")

print(importance)

importance.to_csv(

    os.path.join(

        REPORT_FOLDER,

        "feature_importance.csv"

    ),

    index=False

)

print("\n" + "=" * 60)
print("TRAINING COMPLETED")
print("=" * 60)

print("Model : refinery_model.pkl")

print("Accuracy :", round(
    accuracy * 100,
    2
), "%")
