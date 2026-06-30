import os
import sys
import random
import pandas as pd
import numpy as np

# ----------------------------------------------------
# Add project root to Python path
# ----------------------------------------------------
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

PROJECT_ROOT = os.path.abspath(
    os.path.join(CURRENT_DIR, "..", "..", "..")
)

sys.path.append(PROJECT_ROOT)

from data.engineering_limits import ENGINEERING_LIMITS
# ======================================================
# DATASET CONFIGURATION
# ======================================================

TOTAL_RECORDS = 75000

HEALTHY_PERCENT = 0.60
WARNING_PERCENT = 0.20
CRITICAL_PERCENT = 0.125
FAILURE_PERCENT = 0.075

EQUIPMENT_TYPES = list(ENGINEERING_LIMITS.keys())

RECORDS_PER_EQUIPMENT = TOTAL_RECORDS // len(EQUIPMENT_TYPES)
COLUMNS = [

    "Equipment_Type",

    "Temperature",

    "Pressure",

    "Vibration",

    "Operating_Hours",

    "Failure_Class"

]
def random_value(low, high):

    return round(random.uniform(low, high), 2)
def generate_runtime(expected_life, condition):

    """
    expected_life is in years.

    We convert it into operating hours.

    Approximation:
    1 year = 8760 hours
    """

    total_hours = expected_life * 8760

    if condition == "Healthy":

        return random.randint(
            int(total_hours * 0.05),
            int(total_hours * 0.40)
        )

    elif condition == "Warning":

        return random.randint(
            int(total_hours * 0.40),
            int(total_hours * 0.65)
        )

    elif condition == "Critical":

        return random.randint(
            int(total_hours * 0.65),
            int(total_hours * 0.90)
        )

    else:

        return random.randint(
            int(total_hours * 0.90),
            int(total_hours * 1.15)
        )
    
def get_sensor_range(low, high, warning, alarm, condition):
    """
    Generate realistic sensor values based on equipment condition.
    """

    # Equipment doesn't have this sensor
    if low is None or high is None:
        return None

    # -------------------- Healthy --------------------
    if condition == "Healthy":

        upper = warning if warning else high * 0.8

        return random_value(low, upper * 0.90)

    # -------------------- Warning --------------------
    elif condition == "Warning":

        if warning is None:
            return random_value(low, high)

        return random_value(
            warning * 0.90,
            warning
        )

    # -------------------- Critical --------------------
    elif condition == "Critical":

        if warning is None or alarm is None:
            return random_value(low, high)

        return random_value(
            warning,
            alarm
        )

    # -------------------- Failure --------------------

    else:

        if alarm is None:
            return random_value(low, high)

        return random_value(
            alarm,
            alarm * 1.10
        )
def generate_sample(equipment_type, condition):

    specs = ENGINEERING_LIMITS[equipment_type]

    runtime = generate_runtime(
        specs["expected_life_years"],
        condition
    )

    sensors = {}

    sensor_list = []

    if specs["temperature"] is not None:
        sensor_list.append("temperature")

    if specs["pressure"] is not None:
        sensor_list.append("pressure")

    if specs["vibration"] is not None:
        sensor_list.append("vibration")

    # Choose abnormal sensors
    abnormal = []

    if condition == "Warning":

        abnormal = random.sample(
            sensor_list,
            min(1, len(sensor_list))
        )

    elif condition == "Critical":

        abnormal = random.sample(
            sensor_list,
            min(2, len(sensor_list))
        )

    elif condition == "Failure":

        abnormal = sensor_list

    # ---------------- Temperature ----------------

    if specs["temperature"] is not None:

        if "temperature" in abnormal:

            sensors["Temperature"] = get_sensor_range(
                specs["temperature"][0],
                specs["temperature"][1],
                specs["warning_temperature"],
                specs["alarm_temperature"],
                condition
            )

        else:

            sensors["Temperature"] = random_value(
                specs["temperature"][0],
                specs["warning_temperature"] * 0.85
            )

    # ---------------- Pressure ----------------

    if specs["pressure"] is None:

        sensors["Pressure"] = 0

    else:

        if "pressure" in abnormal:

            sensors["Pressure"] = get_sensor_range(
                specs["pressure"][0],
                specs["pressure"][1],
                specs["warning_pressure"],
                specs["alarm_pressure"],
                condition
            )

        else:

            sensors["Pressure"] = random_value(
                specs["pressure"][0],
                specs["warning_pressure"] * 0.85
            )

    # ---------------- Vibration ----------------

    if specs["vibration"] is None:

        sensors["Vibration"] = 0

    else:

        if "vibration" in abnormal:

            sensors["Vibration"] = get_sensor_range(
                specs["vibration"][0],
                specs["vibration"][1],
                specs["warning_vibration"],
                specs["alarm_vibration"],
                condition
            )

        else:

            sensors["Vibration"] = random_value(
                specs["vibration"][0],
                specs["warning_vibration"] * 0.85
            )

    return {

        "Equipment_Type": equipment_type,

        "Temperature": sensors["Temperature"],

        "Pressure": sensors["Pressure"],

        "Vibration": sensors["Vibration"],

        "Operating_Hours": runtime,

        "Failure_Class": condition

    }
def generate_sample(equipment_type, condition):

    specs = ENGINEERING_LIMITS[equipment_type]

    runtime = generate_runtime(
        specs["expected_life_years"],
        condition
    )

    sensors = {}

    sensor_list = []

    if specs["temperature"] is not None:
        sensor_list.append("temperature")

    if specs["pressure"] is not None:
        sensor_list.append("pressure")

    if specs["vibration"] is not None:
        sensor_list.append("vibration")

    # Choose abnormal sensors
    abnormal = []

    if condition == "Warning":

        abnormal = random.sample(
            sensor_list,
            min(1, len(sensor_list))
        )

    elif condition == "Critical":

        abnormal = random.sample(
            sensor_list,
            min(2, len(sensor_list))
        )

    elif condition == "Failure":

        abnormal = sensor_list

    # ---------------- Temperature ----------------

    if specs["temperature"] is not None:

        if "temperature" in abnormal:

            sensors["Temperature"] = get_sensor_range(
                specs["temperature"][0],
                specs["temperature"][1],
                specs["warning_temperature"],
                specs["alarm_temperature"],
                condition
            )

        else:

            sensors["Temperature"] = random_value(
                specs["temperature"][0],
                specs["warning_temperature"] * 0.85
            )

    # ---------------- Pressure ----------------

    if specs["pressure"] is None:

        sensors["Pressure"] = 0

    else:

        if "pressure" in abnormal:

            sensors["Pressure"] = get_sensor_range(
                specs["pressure"][0],
                specs["pressure"][1],
                specs["warning_pressure"],
                specs["alarm_pressure"],
                condition
            )

        else:

            sensors["Pressure"] = random_value(
                specs["pressure"][0],
                specs["warning_pressure"] * 0.85
            )

    # ---------------- Vibration ----------------

    if specs["vibration"] is None:

        sensors["Vibration"] = 0

    else:

        if "vibration" in abnormal:

            sensors["Vibration"] = get_sensor_range(
                specs["vibration"][0],
                specs["vibration"][1],
                specs["warning_vibration"],
                specs["alarm_vibration"],
                condition
            )

        else:

            sensors["Vibration"] = random_value(
                specs["vibration"][0],
                specs["warning_vibration"] * 0.85
            )

    return {

        "Equipment_Type": equipment_type,

        "Temperature": sensors["Temperature"],

        "Pressure": sensors["Pressure"],

        "Vibration": sensors["Vibration"],

        "Operating_Hours": runtime,

        "Failure_Class": condition

    }
    
def generate_dataset():

    dataset = []

    distribution = {

        "Healthy": int(RECORDS_PER_EQUIPMENT * HEALTHY_PERCENT),

        "Warning": int(RECORDS_PER_EQUIPMENT * WARNING_PERCENT),

        "Critical": int(RECORDS_PER_EQUIPMENT * CRITICAL_PERCENT),

        "Failure": RECORDS_PER_EQUIPMENT
                    - int(RECORDS_PER_EQUIPMENT * HEALTHY_PERCENT)
                    - int(RECORDS_PER_EQUIPMENT * WARNING_PERCENT)
                    - int(RECORDS_PER_EQUIPMENT * CRITICAL_PERCENT)

    }

    for equipment in EQUIPMENT_TYPES:

        print(f"Generating {equipment}...")

        for condition, count in distribution.items():

            for _ in range(count):

                dataset.append(

                    generate_sample(
                        equipment,
                        condition
                    )

                )

    df = pd.DataFrame(dataset)

    return df
def shuffle_dataset(df):

    return df.sample(
        frac=1,
        random_state=42
    ).reset_index(drop=True)
def save_dataset(df):

    current_directory = os.path.dirname(
        os.path.abspath(__file__)
    )

    dataset_folder = os.path.join(

        current_directory,

        "..",

        "dataset",

        "raw"

    )

    os.makedirs(
        dataset_folder,
        exist_ok=True
    )

    output_file = os.path.join(

        dataset_folder,

        "refinery_dataset.csv"

    )

    df.to_csv(

        output_file,

        index=False

    )

    return output_file
if __name__ == "__main__":

    print("=" * 60)
    print("REFINERY DATASET GENERATION")
    print("=" * 60)

    df = generate_dataset()

    df = shuffle_dataset(df)

    output = save_dataset(df)

    print("\nDataset Generated Successfully!\n")

    print(df.head())

    print("\nDataset Shape")

    print(df.shape)

    print("\nEquipment Distribution")

    print(df["Equipment_Type"].value_counts())

    print("\nFailure Distribution")

    print(df["Failure_Class"].value_counts())

    print("\nSaved To")

    print(output)

    print("\nGeneration Complete.")
