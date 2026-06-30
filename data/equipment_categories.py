"""
Master Asset Configuration
Used by:
1. seed_equipment.py
2. Equipment Search API
3. Digital Twin
4. Dashboard
"""

# ============================================================
# REFINERY UNITS
# ============================================================

REFINERY_UNITS = {

    "CDU": {
        "name": "Crude Distillation Unit",
        "sections": {
            "FH": "Feed Handling",
            "PT": "Preheat Train",
            "MF": "Main Fractionator",
            "PH": "Pump House"
        }
    },

    "VDU": {
        "name": "Vacuum Distillation Unit",
        "sections": {
            "VH": "Vacuum Heater",
            "VC": "Vacuum Column",
            "BP": "Bottom Pumps"
        }
    },

    "FCC": {
        "name": "Fluid Catalytic Cracking Unit",
        "sections": {
            "RC": "Reactor",
            "RG": "Regenerator",
            "FR": "Fractionator"
        }
    },

    "HCU": {
        "name": "Hydrocracker Unit",
        "sections": {
            "RS": "Reaction Section",
            "RG": "Recycle Gas",
            "HF": "Hydrogen Feed"
        }
    },

    "DHDT": {
        "name": "Diesel Hydrotreater",
        "sections": {
            "FS": "Feed Section",
            "RS": "Reaction Section"
        }
    },

    "NHT": {
        "name": "Naphtha Hydrotreater",
        "sections": {
            "FS": "Feed Section",
            "RS": "Reaction Section"
        }
    },

    "HGU": {
        "name": "Hydrogen Generation Unit",
        "sections": {
            "RF": "Reformer",
            "PS": "PSA Unit"
        }
    },

    "SRU": {
        "name": "Sulfur Recovery Unit",
        "sections": {
            "RF": "Reaction Furnace",
            "TG": "Tail Gas"
        }
    },

    "UTL": {
        "name": "Utilities",
        "sections": {
            "CA": "Compressed Air",
            "SD": "Steam Distribution",
            "WS": "Water Supply"
        }
    },

    "CT": {
        "name": "Cooling Tower",
        "sections": {
            "CA": "Cooling Cell A",
            "CB": "Cooling Cell B"
        }
    },

    "BH": {
        "name": "Boiler House",
        "sections": {
            "SG": "Steam Generation",
            "WT": "Water Treatment"
        }
    },

    "TF": {
        "name": "Tank Farm",
        "sections": {
            "NT": "North Tank Farm",
            "ST": "South Tank Farm"
        }
    },

    "PP": {
        "name": "Power Plant",
        "sections": {
            "GH": "Generator Hall",
            "TH": "Turbine Hall"
        }
    }

}

# ============================================================
# EQUIPMENT CATEGORIES
# ============================================================

EQUIPMENT_CATEGORIES = {

    "PM": {
        "name": "Pump",
        "count": 120,
        "manufacturers": [
            "Flowserve",
            "KSB",
            "Kirloskar",
            "Sulzer",
            "Grundfos"
        ],
        "model_prefix": {
            "Flowserve": "FS",
            "KSB": "KSB",
            "Kirloskar": "KIR",
            "Sulzer": "SZ",
            "Grundfos": "GF"
        }
    },

    "CP": {
        "name": "Compressor",
        "count": 80,
        "manufacturers": [
            "Atlas Copco",
            "Ingersoll Rand",
            "Siemens Energy"
        ],
        "model_prefix": {
            "Atlas Copco": "AC",
            "Ingersoll Rand": "IR",
            "Siemens Energy": "SE"
        }
    },

    "MT": {
        "name": "Motor",
        "count": 120,
        "manufacturers": [
            "ABB",
            "Siemens",
            "WEG",
            "CG Power"
        ],
        "model_prefix": {
            "ABB": "ABB",
            "Siemens": "SIM",
            "WEG": "WEG",
            "CG Power": "CG"
        }
    },

    "HX": {
        "name": "Heat Exchanger",
        "count": 80,
        "manufacturers": [
            "Alfa Laval",
            "Kelvion",
            "Danfoss"
        ],
        "model_prefix": {
            "Alfa Laval": "AL",
            "Kelvion": "KL",
            "Danfoss": "DF"
        }
    },

    "VL": {
        "name": "Valve",
        "count": 220,
        "manufacturers": [
            "Emerson",
            "Fisher",
            "L&T Valves",
            "Forbes Marshall"
        ],
        "model_prefix": {
            "Emerson": "EM",
            "Fisher": "FSH",
            "L&T Valves": "LTV",
            "Forbes Marshall": "FM"
        }
    },

    "FN": {
        "name": "Furnace",
        "count": 25,
        "manufacturers": [
            "John Zink",
            "Honeywell"
        ],
        "model_prefix": {
            "John Zink": "JZ",
            "Honeywell": "HW"
        }
    },

    "BL": {
        "name": "Boiler",
        "count": 25,
        "manufacturers": [
            "Thermax",
            "BHEL"
        ],
        "model_prefix": {
            "Thermax": "THX",
            "BHEL": "BHL"
        }
    },

    "TB": {
        "name": "Turbine",
        "count": 20,
        "manufacturers": [
            "Siemens Energy",
            "GE"
        ],
        "model_prefix": {
            "Siemens Energy": "SE",
            "GE": "GE"
        }
    },

    "RC": {
        "name": "Reactor",
        "count": 40,
        "manufacturers": [
            "UOP",
            "Shell"
        ],
        "model_prefix": {
            "UOP": "UOP",
            "Shell": "SH"
        }
    },

    "DC": {
        "name": "Distillation Column",
        "count": 30,
        "manufacturers": [
            "L&T",
            "Technip"
        ],
        "model_prefix": {
            "L&T": "LT",
            "Technip": "TEC"
        }
    },

    "TK": {
        "name": "Storage Tank",
        "count": 50,
        "manufacturers": [
            "L&T",
            "Toyo Engineering"
        ],
        "model_prefix": {
            "L&T": "LT",
            "Toyo Engineering": "TY"
        }
    },

    "CS": {
        "name": "Cooling System",
        "count": 40,
        "manufacturers": [
            "SPX Cooling",
            "Baltimore Aircoil"
        ],
        "model_prefix": {
            "SPX Cooling": "SPX",
            "Baltimore Aircoil": "BAC"
        }
    },

    "GN": {
        "name": "Generator",
        "count": 20,
        "manufacturers": [
            "Cummins",
            "Caterpillar",
            "Kirloskar"
        ],
        "model_prefix": {
            "Cummins": "CM",
            "Caterpillar": "CAT",
            "Kirloskar": "KIR"
        }
    },

    "PI": {
        "name": "Pipeline",
        "count": 60,
        "manufacturers": [
            "Jindal",
            "Tata Steel"
        ],
        "model_prefix": {
            "Jindal": "JSL",
            "Tata Steel": "TSL"
        }
    },

    "IN": {
        "name": "Instrumentation",
        "count": 150,
        "manufacturers": [
            "Honeywell",
            "ABB",
            "Yokogawa",
            "Emerson"
        ],
        "model_prefix": {
            "Honeywell": "HW",
            "ABB": "ABB",
            "Yokogawa": "YK",
            "Emerson": "EM"
        }
    }

}