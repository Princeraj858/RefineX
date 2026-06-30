import os
import sys

import joblib
import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

PROJECT_ROOT = os.path.abspath(
    os.path.join(
        CURRENT_DIR,
        "..",
        "..",
        ".."
    )
)

sys.path.append(PROJECT_ROOT)
DATASET_PATH = os.path.join(

    CURRENT_DIR,

    "..",

    "dataset",

    "raw",

    "refinery_dataset.csv"

)

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

os.makedirs(PROCESSED_FOLDER, exist_ok=True)

os.makedirs(MODEL_FOLDER, exist_ok=True)
print("=" * 60)
print("Reading Dataset...")
print("=" * 60)

df = pd.read_csv(DATASET_PATH)

print(df.head())

print()

print(df.shape)
df.fillna(0, inplace=True)
equipment_encoder = LabelEncoder()

df["Equipment_Type"] = equipment_encoder.fit_transform(

    df["Equipment_Type"]

)
label_encoder = LabelEncoder()

df["Failure_Class"] = label_encoder.fit_transform(

    df["Failure_Class"]

)
joblib.dump(

    equipment_encoder,

    os.path.join(

        MODEL_FOLDER,

        "equipment_encoder.pkl"

    )

)

joblib.dump(

    label_encoder,

    os.path.join(

        MODEL_FOLDER,

        "label_encoder.pkl"

    )

)
# ======================================================
# FEATURES AND TARGET
# ======================================================

X = df[[
    "Equipment_Type",
    "Temperature",
    "Pressure",
    "Vibration",
    "Operating_Hours"
]]

y = df["Failure_Class"]

print("\nFeatures Shape :", X.shape)
print("Target Shape   :", y.shape)

# ======================================================
# SCALE ONLY NUMERICAL FEATURES
# ======================================================

scaler = StandardScaler()

sensor_columns = [

    "Temperature",

    "Pressure",

    "Vibration",

    "Operating_Hours"

]

X[sensor_columns] = scaler.fit_transform(

    X[sensor_columns]

)

joblib.dump(

    scaler,

    os.path.join(

        MODEL_FOLDER,

        "scaler.pkl"

    )

)

# ======================================================
# TRAIN TEST SPLIT
# ======================================================

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.20,

    random_state=42,

    stratify=y

)

train_data = X_train.copy()
train_data["Failure_Class"] = y_train

test_data = X_test.copy()
test_data["Failure_Class"] = y_test

train_data.to_csv(

    os.path.join(

        PROCESSED_FOLDER,

        "train_dataset.csv"

    ),

    index=False

)

test_data.to_csv(

    os.path.join(

        PROCESSED_FOLDER,

        "test_dataset.csv"

    ),

    index=False

)

print("\n" + "=" * 60)
print("PREPROCESSING COMPLETED")
print("=" * 60)

print("\nTraining Samples :", len(train_data))
print("Testing Samples  :", len(test_data))

print("\nSaved Files")

print("✔ equipment_encoder.pkl")
print("✔ label_encoder.pkl")
print("✔ scaler.pkl")
print("✔ train_dataset.csv")
print("✔ test_dataset.csv")