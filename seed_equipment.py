"""
===========================================================
Smart Refinery AI
Equipment Master Generator

Generates realistic refinery equipment and inserts
them into MongoDB Atlas.

Author : Sneha
===========================================================
"""

import os
import json
import random
from collections import defaultdict
from pymongo import MongoClient
from dotenv import load_dotenv

from data.equipment_categories import EQUIPMENT_CATEGORIES, REFINERY_UNITS
from data.equipment_names import *
from data.engineering_limits import ENGINEERING_LIMITS
from data.generator_utils import (
    installation_date,
    commissioning_date,
    serial_number,
    model_number,
    health_index,
    equipment_status,
    criticality,
    maintenance_dates,
    rated_value,
    rated_rpm,
    power_rating
)
from data.equipment_mapping import EQUIPMENT_LOCATION_MAP


# ===========================================================
# MongoDB Connection
# ===========================================================

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
try:
    client.admin.command("ping")
    print("MongoDB Connected Successfully.")
except Exception as e:
    print(e)
    exit()
db = client["smart_refinery_ai"]

equipment_collection = db["equipment"]


# ===========================================================
# Clear Existing Equipment
# ===========================================================

equipment_collection.delete_many({})

print("\nOld equipment removed.")


# ===========================================================
# Equipment Name Dictionary
# ===========================================================

CATEGORY_NAME_MAP = {

    "Pump": PUMP_NAMES,

    "Compressor": COMPRESSOR_NAMES,

    "Motor": MOTOR_NAMES,

    "Heat Exchanger": HEAT_EXCHANGER_NAMES,

    "Valve": VALVE_NAMES,

    "Boiler": BOILER_NAMES,

    "Furnace": FURNACE_NAMES,

    "Turbine": TURBINE_NAMES,

    "Reactor": REACTOR_NAMES,

    "Distillation Column": COLUMN_NAMES,

    "Storage Tank": TANK_NAMES,

    "Cooling System": COOLING_SYSTEM_NAMES,

    "Generator": GENERATOR_NAMES,

    "Pipeline": PIPELINE_NAMES,

    "Instrumentation": INSTRUMENT_NAMES

}


# ===========================================================
# Runtime Containers
# ===========================================================

equipment_documents = []

used_equipment_ids = set()

used_serial_numbers = set()

asset_counter = defaultdict(int)

name_counter = defaultdict(int)


# ===========================================================
# Equipment Name Generator
# Cycles through names evenly
# ===========================================================

def get_equipment_name(category):

    names = CATEGORY_NAME_MAP[category]

    index = name_counter[category] % len(names)

    name_counter[category] += 1

    return names[index]


# ===========================================================
# Equipment Location
# ===========================================================

def get_location(equipment_name):

    return random.choice(
        EQUIPMENT_LOCATION_MAP[equipment_name]
    )


# ===========================================================
# Equipment ID Generator
# Example:
# PM-CDU-FH-001
# ===========================================================

def generate_equipment_id(prefix, unit_code, section_code):

    key = f"{prefix}-{unit_code}-{section_code}"

    asset_counter[key] += 1

    return f"{key}-{asset_counter[key]:03}"


# ===========================================================
# Manufacturer Generator
# ===========================================================

def get_manufacturer(category):

    for data in EQUIPMENT_CATEGORIES.values():

        if data["name"] == category:

            return random.choice(
                data["manufacturers"]
            )

    return "Unknown"


# ===========================================================
# Model Generator
# ===========================================================

def get_model(category, manufacturer):

    for data in EQUIPMENT_CATEGORIES.values():

        if data["name"] == category:

            prefix = data["model_prefix"][manufacturer]

            return model_number(prefix)

    return "UNKNOWN-0000"


print("Initialisation Complete.\n")

# ===========================================================
# Equipment Document Builder
# ===========================================================

def create_equipment_document(prefix, category):

    # -------------------------------------------------------
    # Basic Details
    # -------------------------------------------------------

    equipment_name = get_equipment_name(category)

    unit_code, section_code = get_location(equipment_name)

    unit_name = REFINERY_UNITS[unit_code]["name"]

    section_name = REFINERY_UNITS[unit_code]["sections"][section_code]

    equipment_id = generate_equipment_id(
        prefix,
        unit_code,
        section_code
    )

    # Prevent duplicate Equipment IDs
    while equipment_id in used_equipment_ids:
        equipment_id = generate_equipment_id(
            prefix,
            unit_code,
            section_code
        )

    used_equipment_ids.add(equipment_id)

    manufacturer = get_manufacturer(category)

    model = get_model(
        category,
        manufacturer
    )

    serial = serial_number()

    while serial in used_serial_numbers:
        serial = serial_number()

    used_serial_numbers.add(serial)

    # -------------------------------------------------------
    # Dates
    # -------------------------------------------------------

    install_date = installation_date()

    commission_date = commissioning_date(
        install_date
    )

    install_year = install_date.year

    # -------------------------------------------------------
    # Equipment Health
    # -------------------------------------------------------

    health = health_index(
        install_year
    )

    status = equipment_status()

    critical = criticality()

    # -------------------------------------------------------
    # Engineering Limits
    # -------------------------------------------------------

    limits = ENGINEERING_LIMITS[category]

    rated_temperature = rated_value(
        limits["temperature"]
    )

    rated_pressure = rated_value(
        limits["pressure"]
    )

    rated_vibration = rated_value(
        limits["vibration"]
    )

    rated_rpm_value = rated_rpm(
        limits["rpm"]
    )

    rated_power = power_rating(
        limits["power_kw"]
    )

    # -------------------------------------------------------
    # Maintenance
    # -------------------------------------------------------

    last_maintenance, next_maintenance = maintenance_dates(
        limits["maintenance_days"]
    )

    # -------------------------------------------------------
    # Equipment Document
    # -------------------------------------------------------

    document = {

        "equipment_id": equipment_id,

        "equipment_name": equipment_name,

        "category": category,

        "manufacturer": manufacturer,

        "model": model,

        "serial_number": serial,

        "unit_code": unit_code,

        "unit": unit_name,

        "section_code": section_code,

        "section": section_name,

        "installation_year": install_year,

        "installation_date":
            install_date.strftime("%Y-%m-%d"),

        "commissioned_on":
            commission_date.strftime("%Y-%m-%d"),

        "status": status,

        "criticality": critical,

        "health_index": health,

        "rated_temperature": rated_temperature,

        "warning_temperature":
            limits["warning_temperature"],

        "alarm_temperature":
            limits["alarm_temperature"],

        "rated_pressure": rated_pressure,

        "warning_pressure":
            limits["warning_pressure"],

        "alarm_pressure":
            limits["alarm_pressure"],

        "rated_vibration": rated_vibration,

        "warning_vibration":
            limits["warning_vibration"],

        "alarm_vibration":
            limits["alarm_vibration"],

        "rated_rpm": rated_rpm_value,

        "power_rating_kw": rated_power,

        "maintenance_frequency_days":
            limits["maintenance_days"],

        "inspection_frequency_days":
            limits["inspection_days"],

        "lubrication_frequency_days":
            limits["lubrication_days"],

        "expected_life_years":
            limits["expected_life_years"],

        "last_maintenance":
            last_maintenance,

        "next_maintenance":
            next_maintenance,

        "created_at":
            install_date.strftime("%Y-%m-%d")

    }

    return document
# ===========================================================
# Generate Equipment Master
# ===========================================================

print("=" * 70)
print("Generating Equipment Master...")
print("=" * 70)

category_summary = {}

for prefix, info in EQUIPMENT_CATEGORIES.items():

    category = info["name"]

    total_assets = info["count"]

    category_summary[category] = 0

    print(f"\nGenerating {total_assets} {category} assets...")

    for _ in range(total_assets):

        equipment = create_equipment_document(
            prefix,
            category
        )

        # --------------------------------------------------
        # Dashboard / Future ML Fields
        # --------------------------------------------------

        health = equipment["health_index"]

        if health >= 95:
            condition = "Healthy"

        elif health >= 85:
            condition = "Monitor"

        else:
            condition = "Critical"

        equipment.update({

            "is_active": True,

            "current_condition": condition,

            "maintenance_history": [],

            "prediction_history": [],

            "incident_history": [],

            "sensor_history": [],

            "created_by": "Equipment Generator",

            "last_prediction": None,

            "remarks": ""

        })

        equipment_documents.append(equipment)

        category_summary[category] += 1


print("\nEquipment Generation Completed.")


# ===========================================================
# Export JSON Backup
# ===========================================================

print("\nCreating equipment_master.json ...")

with open(
    "equipment_master.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(

        equipment_documents,

        file,

        indent=4,

        default=str

    )

print("JSON Backup Created Successfully.")


# ===========================================================
# Generate Statistics
# ===========================================================

manufacturer_stats = defaultdict(int)

unit_stats = defaultdict(int)

status_stats = defaultdict(int)

condition_stats = defaultdict(int)

for equipment in equipment_documents:

    manufacturer_stats[
        equipment["manufacturer"]
    ] += 1

    unit_stats[
        equipment["unit"]
    ] += 1

    status_stats[
        equipment["status"]
    ] += 1

    condition_stats[
        equipment["current_condition"]
    ] += 1


print("\nGeneration Statistics Ready.")
# ===========================================================
# Insert Equipment into MongoDB
# ===========================================================

print("\n" + "=" * 70)
print("Uploading Equipment to MongoDB...")
print("=" * 70)

if equipment_documents:

    equipment_collection.insert_many(equipment_documents)

print(f"\nInserted {len(equipment_documents)} documents successfully.")


# ===========================================================
# Verify Database Count
# ===========================================================

db_count = equipment_collection.count_documents({})

print(f"MongoDB Collection Count : {db_count}")


# ===========================================================
# Category Summary
# ===========================================================

print("\n" + "=" * 70)
print("CATEGORY SUMMARY")
print("=" * 70)

for category, count in sorted(category_summary.items()):

    print(f"{category:<25} : {count}")


# ===========================================================
# Manufacturer Summary
# ===========================================================

print("\n" + "=" * 70)
print("MANUFACTURER SUMMARY")
print("=" * 70)

for manufacturer, count in sorted(manufacturer_stats.items()):

    print(f"{manufacturer:<25} : {count}")


# ===========================================================
# Refinery Unit Summary
# ===========================================================

print("\n" + "=" * 70)
print("REFINERY UNIT SUMMARY")
print("=" * 70)

for unit, count in sorted(unit_stats.items()):

    print(f"{unit:<35} : {count}")


# ===========================================================
# Equipment Status Summary
# ===========================================================

print("\n" + "=" * 70)
print("STATUS SUMMARY")
print("=" * 70)

for status, count in sorted(status_stats.items()):

    print(f"{status:<25} : {count}")


# ===========================================================
# Health Summary
# ===========================================================

print("\n" + "=" * 70)
print("HEALTH SUMMARY")
print("=" * 70)

for condition, count in sorted(condition_stats.items()):

    print(f"{condition:<25} : {count}")


# ===========================================================
# Sample Equipment
# ===========================================================

print("\n" + "=" * 70)
print("SAMPLE EQUIPMENT")
print("=" * 70)

for equipment in equipment_documents[:5]:

    print()

    print(f"ID          : {equipment['equipment_id']}")
    print(f"Equipment   : {equipment['equipment_name']}")
    print(f"Category    : {equipment['category']}")
    print(f"Unit        : {equipment['unit']}")
    print(f"Section     : {equipment['section']}")
    print(f"Health      : {equipment['health_index']}%")
    print(f"Condition   : {equipment['current_condition']}")
    print(f"Status      : {equipment['status']}")


# ===========================================================
# Final Summary
# ===========================================================

print("\n" + "=" * 70)
print("EQUIPMENT MASTER CREATED SUCCESSFULLY")
print("=" * 70)

print(f"Total Equipment Generated : {len(equipment_documents)}")
print(f"MongoDB Collection        : equipment")
print(f"Database                  : smart_refinery_ai")
print("JSON Backup               : equipment_master.json")

print("\nYour Equipment Master is ready for:")

print("✔ Predictive Maintenance")
print("✔ Equipment Autocomplete")
print("✔ Dashboard")
print("✔ Incident Tracking")
print("✔ Digital Twin")
print("✔ Maintenance Scheduler")

print("\nDone.\n")