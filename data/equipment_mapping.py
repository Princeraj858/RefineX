"""
Equipment Location Mapping

Maps each equipment type to the refinery units and sections
where it is normally installed.
"""

EQUIPMENT_LOCATION_MAP = {

# ==========================================================
# PUMPS
# ==========================================================

"Crude Oil Charge Pump": [
    ("CDU", "FH")
],

"Crude Oil Feed Pump": [
    ("CDU", "FH")
],

"Atmospheric Residue Pump": [
    ("CDU", "PH")
],

"Vacuum Residue Pump": [
    ("VDU", "BP")
],

"Vacuum Gas Oil Pump": [
    ("VDU", "BP")
],

"Heavy Gas Oil Pump": [
    ("FCC", "FR"),
    ("HCU", "RS")
],

"Light Gas Oil Pump": [
    ("FCC", "FR")
],

"Diesel Product Pump": [
    ("DHDT", "FS"),
    ("TF", "NT")
],

"Diesel Transfer Pump": [
    ("TF", "NT"),
    ("TF", "ST")
],

"Kerosene Transfer Pump": [
    ("TF", "NT")
],

"Naphtha Transfer Pump": [
    ("NHT", "FS"),
    ("TF", "ST")
],

"LPG Transfer Pump": [
    ("TF", "ST")
],

"Fuel Oil Transfer Pump": [
    ("TF", "NT")
],

"Bottom Product Pump": [
    ("CDU", "MF"),
    ("VDU", "VC")
],

"Overhead Product Pump": [
    ("CDU", "MF")
],

"Boiler Feed Water Pump": [
    ("BH", "SG")
],

"Condensate Pump": [
    ("BH", "WT")
],

"Cooling Water Pump": [
    ("CT", "CA"),
    ("CT", "CB")
],

"Fire Water Pump": [
    ("UTL", "WS"),
    ("TF", "NT")
],

"Utility Water Pump": [
    ("UTL", "WS")
],

"Seal Water Pump": [
    ("UTL", "WS")
],

"Wash Water Pump": [
    ("CDU", "FH"),
    ("VDU", "VH")
],

"Chemical Injection Pump": [
    ("DHDT", "RS"),
    ("NHT", "RS"),
    ("HCU", "RS")
],

"Amine Circulation Pump": [
    ("SRU", "TG")
],

"Caustic Transfer Pump": [
    ("UTL", "WS")
],

"Slop Oil Pump": [
    ("TF", "ST")
],

"Recycle Oil Pump": [
    ("FCC", "RC")
],

"Feed Circulation Pump": [
    ("CDU", "PT"),
    ("VDU", "VC")
],

"Charge Pump": [
    ("CDU", "FH")
],

"Process Water Pump": [
    ("UTL", "WS")
],

# ==========================================================
# COMPRESSORS
# ==========================================================

"Hydrogen Compressor": [
    ("HCU", "HF"),
    ("HGU", "RF")
],

"Recycle Gas Compressor": [
    ("HCU", "RG")
],

"Wet Gas Compressor": [
    ("FCC", "RC")
],

"Fuel Gas Compressor": [
    ("FCC", "FR"),
    ("HCU", "HF")
],

"Instrument Air Compressor": [
    ("UTL", "CA")
],

"Plant Air Compressor": [
    ("UTL", "CA")
],

"Nitrogen Compressor": [
    ("UTL", "CA")
],

"Booster Compressor": [
    ("HGU", "RF")
],

"LPG Compressor": [
    ("TF", "ST")
],

"Process Gas Compressor": [
    ("HCU", "RS"),
    ("FCC", "RC")
],

"Hydrogen Booster Compressor": [
    ("HGU", "RF")
],

"Flare Gas Recovery Compressor": [
    ("SRU", "TG")
],

"Off Gas Compressor": [
    ("FCC", "FR")
],

"Sour Gas Compressor": [
    ("SRU", "TG")
],

"Air Blower Compressor": [
    ("UTL", "CA")
],
# ==========================================================
# MOTORS
# ==========================================================

"Pump Drive Motor": [
    ("CDU", "PH"),
    ("VDU", "BP")
],

"Compressor Drive Motor": [
    ("HCU", "RS"),
    ("HGU", "RF")
],

"Cooling Fan Motor": [
    ("CT", "CA"),
    ("CT", "CB")
],

"Cooling Tower Motor": [
    ("CT", "CA"),
    ("CT", "CB")
],

"Boiler Feed Motor": [
    ("BH", "SG")
],

"Forced Draft Fan Motor": [
    ("BH", "SG")
],

"Induced Draft Fan Motor": [
    ("BH", "SG")
],

"Blower Motor": [
    ("FCC", "RG")
],

"Transfer Pump Motor": [
    ("TF", "NT"),
    ("TF", "ST")
],

"Hydraulic Motor": [
    ("HCU", "RS")
],

"Cooling Pump Motor": [
    ("CT", "CA")
],

"Vacuum Pump Motor": [
    ("VDU", "VH")
],

"Agitator Motor": [
    ("SRU", "RF")
],

"Conveyor Drive Motor": [
    ("UTL", "WS")
],

"Exhaust Fan Motor": [
    ("PP", "GH")
],

# ==========================================================
# HEAT EXCHANGERS
# ==========================================================

"Crude Oil Preheater": [
    ("CDU", "PT")
],

"Feed Heat Exchanger": [
    ("HCU", "HF"),
    ("DHDT", "FS")
],

"Feed Effluent Heat Exchanger": [
    ("HCU", "RS")
],

"Product Cooler": [
    ("FCC", "FR")
],

"Diesel Cooler": [
    ("DHDT", "FS")
],

"Naphtha Cooler": [
    ("NHT", "FS")
],

"Kerosene Cooler": [
    ("CDU", "MF")
],

"Air Cooler": [
    ("FCC", "FR"),
    ("HCU", "HF")
],

"Water Cooler": [
    ("UTL", "WS")
],

"Steam Condenser": [
    ("PP", "TH")
],

"Charge Heater Exchanger": [
    ("CDU", "PT")
],

"Shell and Tube Heat Exchanger": [
    ("CDU", "MF"),
    ("VDU", "VC")
],

"Plate Heat Exchanger": [
    ("UTL", "WS")
],

"Reboiler Heat Exchanger": [
    ("CDU", "MF"),
    ("VDU", "VC")
],

"Interchanger": [
    ("FCC", "FR")
],

# ==========================================================
# VALVES
# ==========================================================

"Control Valve": [
    ("CDU", "MF"),
    ("FCC", "FR"),
    ("HCU", "RS")
],

"Pressure Relief Valve": [
    ("CDU", "MF"),
    ("VDU", "VC"),
    ("BH", "SG")
],

"Safety Relief Valve": [
    ("SRU", "RF"),
    ("HCU", "RS")
],

"Emergency Shutdown Valve": [
    ("HCU", "HF"),
    ("FCC", "RC")
],

"Isolation Valve": [
    ("TF", "NT"),
    ("TF", "ST")
],

"Gate Valve": [
    ("UTL", "WS"),
    ("CDU", "PH")
],

"Globe Valve": [
    ("UTL", "SD")
],

"Ball Valve": [
    ("NHT", "RS")
],

"Butterfly Valve": [
    ("CT", "CA")
],

"Check Valve": [
    ("BH", "SG")
],

"Needle Valve": [
    ("HGU", "RF")
],

"Pressure Control Valve": [
    ("HCU", "RS")
],

"Flow Control Valve": [
    ("CDU", "PT")
],

"Steam Control Valve": [
    ("BH", "SG")
],

"Feed Control Valve": [
    ("CDU", "FH")
],

"Fuel Gas Valve": [
    ("FCC", "FR")
],

"Blowdown Valve": [
    ("BH", "WT")
],

"Drain Valve": [
    ("TF", "ST")
],

"Vent Valve": [
    ("TF", "NT")
],

"Bypass Valve": [
    ("CDU", "MF")
],

"Motor Operated Valve": [
    ("CDU", "PH")
],

"Pneumatic Control Valve": [
    ("FCC", "RC")
],

"Solenoid Valve": [
    ("HCU", "RS")
],

"Emergency Isolation Valve": [
    ("SRU", "TG")
],
# Fix Block Valve mapping
"Block Valve": [
    ("CDU", "PH"),
    ("VDU", "BP"),
    ("UTL", "WS")
],

# ==========================================================
# BOILERS
# ==========================================================

"Steam Boiler": [
    ("BH", "SG")
],

"Waste Heat Boiler": [
    ("FCC", "RG"),
    ("HCU", "RS")
],

"Auxiliary Boiler": [
    ("BH", "SG")
],

"Package Boiler": [
    ("BH", "WT")
],

"High Pressure Boiler": [
    ("BH", "SG")
],

# ==========================================================
# FURNACES
# ==========================================================

"Crude Heater Furnace": [
    ("CDU", "PT")
],

"Vacuum Furnace": [
    ("VDU", "VH")
],

"Charge Heater": [
    ("CDU", "PT")
],

"Reaction Furnace": [
    ("SRU", "RF")
],

"Process Furnace": [
    ("HCU", "RS")
],

"Feed Heater Furnace": [
    ("NHT", "FS")
],

# ==========================================================
# TURBINES
# ==========================================================

"Steam Turbine": [
    ("PP", "TH")
],

"Power Recovery Turbine": [
    ("FCC", "RG")
],

"Generator Turbine": [
    ("PP", "GH")
],

"Utility Turbine": [
    ("UTL", "SD")
],

"Extraction Turbine": [
    ("PP", "TH")
],

# ==========================================================
# REACTORS
# ==========================================================

"Hydrotreater Reactor": [
    ("DHDT", "RS"),
    ("NHT", "RS")
],

"Hydrocracker Reactor": [
    ("HCU", "RS")
],

"Catalytic Reactor": [
    ("FCC", "RC")
],

"Hydrogenation Reactor": [
    ("HCU", "RS")
],

"Desulfurization Reactor": [
    ("SRU", "RF")
],

# ==========================================================
# DISTILLATION COLUMNS
# ==========================================================

"Atmospheric Distillation Column": [
    ("CDU", "MF")
],

"Vacuum Distillation Column": [
    ("VDU", "VC")
],

"Main Fractionator": [
    ("FCC", "FR")
],

"Stripper Column": [
    ("DHDT", "RS")
],

"Stabilizer Column": [
    ("NHT", "RS")
],

"Splitter Column": [
    ("CDU", "MF")
],

# ==========================================================
# STORAGE TANKS
# ==========================================================

"Crude Oil Storage Tank": [
    ("TF", "NT")
],

"Diesel Storage Tank": [
    ("TF", "ST")
],

"Kerosene Storage Tank": [
    ("TF", "ST")
],

"Naphtha Storage Tank": [
    ("TF", "NT")
],

"LPG Storage Tank": [
    ("TF", "ST")
],

"Fuel Oil Storage Tank": [
    ("TF", "NT")
],

"Slop Oil Tank": [
    ("TF", "ST")
],

"Chemical Storage Tank": [
    ("UTL", "WS")
],

"Fire Water Tank": [
    ("UTL", "WS")
],

"Raw Water Tank": [
    ("UTL", "WS")
],

"DM Water Tank": [
    ("BH", "WT")
],

"Foam Tank": [
    ("TF", "NT")
],

# ==========================================================
# COOLING SYSTEMS
# ==========================================================

"Cooling Tower": [
    ("CT", "CA")
],

"Cooling Tower Fan": [
    ("CT", "CA"),
    ("CT", "CB")
],

"Cooling Water Header": [
    ("CT", "CA")
],

"Cooling Water Distribution Pump": [
    ("CT", "CB")
],

"Cooling Cell": [
    ("CT", "CA"),
    ("CT", "CB")
],

"Cooling Basin": [
    ("CT", "CA")
],

# ==========================================================
# GENERATORS
# ==========================================================

"Emergency Diesel Generator": [
    ("PP", "GH")
],

"Standby Generator": [
    ("PP", "GH")
],

"Main Power Generator": [
    ("PP", "GH")
],

"Gas Generator": [
    ("PP", "GH")
],

"Black Start Generator": [
    ("PP", "GH")
],

# ==========================================================
# PIPELINES
# ==========================================================

"Crude Transfer Pipeline": [
    ("CDU", "FH")
],

"Vacuum Residue Pipeline": [
    ("VDU", "BP")
],

"Diesel Pipeline": [
    ("DHDT", "FS")
],

"Fuel Oil Pipeline": [
    ("TF", "NT")
],

"Kerosene Pipeline": [
    ("CDU", "MF")
],

"LPG Pipeline": [
    ("TF", "ST")
],

"Hydrogen Pipeline": [
    ("HGU", "RF"),
    ("HCU", "HF")
],

"Natural Gas Pipeline": [
    ("UTL", "CA")
],

"Steam Pipeline": [
    ("BH", "SG"),
    ("UTL", "SD")
],

"Cooling Water Pipeline": [
    ("CT", "CA"),
    ("UTL", "WS")
],

"Compressed Air Pipeline": [
    ("UTL", "CA")
],

"Fire Water Pipeline": [
    ("UTL", "WS")
],

# ==========================================================
# INSTRUMENTATION
# ==========================================================

"Pressure Transmitter": [
    ("CDU", "FH"),
    ("VDU", "VC"),
    ("HCU", "RS")
],

"Pressure Gauge": [
    ("CDU", "PH"),
    ("BH", "SG")
],

"Pressure Indicator": [
    ("FCC", "FR")
],

"Temperature Transmitter": [
    ("CDU", "PT"),
    ("HCU", "RS")
],

"Temperature Sensor": [
    ("VDU", "VH"),
    ("FCC", "RC")
],

"RTD Sensor": [
    ("BH", "SG")
],

"Thermocouple": [
    ("SRU", "RF")
],

"Flow Meter": [
    ("CDU", "FH"),
    ("UTL", "WS")
],

"Flow Transmitter": [
    ("HCU", "HF")
],

"Flow Indicator": [
    ("FCC", "FR")
],

"Level Transmitter": [
    ("TF", "NT"),
    ("TF", "ST")
],

"Level Gauge": [
    ("TF", "NT")
],

"Level Switch": [
    ("BH", "WT")
],

"Vibration Sensor": [
    ("PP", "TH"),
    ("HCU", "RS")
],

"Speed Sensor": [
    ("PP", "TH")
],

"Current Sensor": [
    ("PP", "GH")
],

"Voltage Sensor": [
    ("PP", "GH")
],

"Gas Detector": [
    ("SRU", "TG"),
    ("TF", "ST")
],

"PLC Controller": [
    ("UTL", "CA")
],

"SCADA Terminal": [
    ("UTL", "CA")
],

"Control Panel": [
    ("PP", "GH")
],

"Analyzer": [
    ("SRU", "TG"),
    ("HGU", "PS")
]
}

