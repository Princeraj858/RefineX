import random
import string
from datetime import datetime, timedelta

# ==========================================================
# Installation Date
# ==========================================================

def installation_date():
    start = datetime(2016,1,1)
    end = datetime(2026,1,1)

    delta = (end - start).days

    return start + timedelta(days=random.randint(0, delta))


# ==========================================================
# Commissioning Date
# ==========================================================

def commissioning_date(install_date):
    days = random.randint(15, 90)
    return install_date + timedelta(days=days)


# ==========================================================
# Serial Number
# Example:
# SN-4D9KX81A
# ==========================================================

def serial_number():

    return "SN-" + "".join(

        random.choices(

            string.ascii_uppercase + string.digits,

            k=8

        )

    )


# ==========================================================
# Model Number
# Example:
# FS-5200
# ABB-930
# ==========================================================

def model_number(prefix):

    return f"{prefix}-{random.randint(1000,9999)}"


# ==========================================================
# Equipment Name Suffix
# ==========================================================

def equipment_suffix(index):

    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    first = letters[index % 26]

    second = ""

    if index >= 26:
        second = str(index // 26)

    return first + second

# ==========================================================
# Health Index
# Based on equipment age
# ==========================================================

def health_index(installation_year):

    current_year = datetime.now().year

    age = current_year - installation_year

    if age <= 2:
        return random.randint(97,100)

    elif age <= 5:
        return random.randint(94,98)

    elif age <= 8:
        return random.randint(90,95)

    else:
        return random.randint(82,91)


# ==========================================================
# Equipment Status
# ==========================================================

def equipment_status():

    return random.choices(

        [

            "Operational",

            "Standby",

            "Under Maintenance"

        ],

        weights=[92,5,3]

    )[0]


# ==========================================================
# Criticality
# ==========================================================

def criticality():

    return random.choices(

        [

            "High",

            "Medium",

            "Low"

        ],

        weights=[40,40,20]

    )[0]


# ==========================================================
# Maintenance Frequency
# ==========================================================

def maintenance_frequency(category):

    mapping = {

        "Pump":180,

        "Motor":180,

        "Compressor":120,

        "Valve":365,

        "Heat Exchanger":365,

        "Boiler":180,

        "Furnace":120,

        "Turbine":120,

        "Reactor":365,

        "Distillation Column":365,

        "Storage Tank":365,

        "Cooling System":180,

        "Generator":180,

        "Pipeline":365,

        "Instrumentation":90

    }

    return mapping.get(category,180)


# ==========================================================
# Inspection Frequency
# ==========================================================

def inspection_frequency(category):

    mapping = {

        "Pump":30,

        "Motor":30,

        "Compressor":30,

        "Valve":90,

        "Heat Exchanger":90,

        "Boiler":30,

        "Furnace":30,

        "Turbine":30,

        "Reactor":60,

        "Distillation Column":90,

        "Storage Tank":180,

        "Cooling System":30,

        "Generator":30,

        "Pipeline":180,

        "Instrumentation":30

    }

    return mapping.get(category,30)


# ==========================================================
# Lubrication Frequency
# ==========================================================

def lubrication_frequency(category):

    mapping = {

        "Pump":60,

        "Motor":90,

        "Compressor":45,

        "Valve":180,

        "Heat Exchanger":None,

        "Boiler":None,

        "Furnace":None,

        "Turbine":45,

        "Reactor":None,

        "Distillation Column":None,

        "Storage Tank":None,

        "Cooling System":60,

        "Generator":60,

        "Pipeline":None,

        "Instrumentation":None

    }

    return mapping.get(category,None)


# ==========================================================
# Maintenance Dates
# ==========================================================

def maintenance_dates(frequency):

    today = datetime.today()

    last = today - timedelta(

        days=random.randint(5, frequency)

    )

    next_due = last + timedelta(days=frequency)

    return (

        last.strftime("%Y-%m-%d"),

        next_due.strftime("%Y-%m-%d")

    )


# ==========================================================
# Random Asset Number
# ==========================================================

def asset_number(number):

    return f"{number:03}"


# ==========================================================
# Random Power Rating
# ==========================================================

def power_rating(values):

    if values is None:
        return None

    return random.choice(values)


# ==========================================================
# Random RPM
# ==========================================================

def rated_rpm(values):

    if values is None:
        return None

    return random.choice(values)


# ==========================================================
# Random Range Value
# ==========================================================

def rated_value(value_range):

    if value_range is None:
        return None

    return round(

        random.uniform(

            value_range[0],

            value_range[1]

        ),

        2

    )