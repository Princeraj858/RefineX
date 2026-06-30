"""
Engineering Design Limits
Used by:
1. seed_equipment.py
2. Predictive Maintenance
3. Dashboard
4. Digital Twin
"""

ENGINEERING_LIMITS = {

# ==========================================================
# PUMPS
# ==========================================================

"Pump":{

"temperature":(40,120),
"warning_temperature":105,
"alarm_temperature":115,

"pressure":(5,25),
"warning_pressure":20,
"alarm_pressure":24,

"vibration":(0.5,4.5),
"warning_vibration":3.5,
"alarm_vibration":4.5,

"rpm":[1450,2900,3600],

"power_kw":[15,22,30,37,45,55,75,90,110],

"maintenance_days":180,

"inspection_days":30,

"lubrication_days":60,

"expected_life_years":20

},

# ==========================================================
# COMPRESSORS
# ==========================================================

"Compressor":{

"temperature":(50,180),
"warning_temperature":160,
"alarm_temperature":175,

"pressure":(15,60),
"warning_pressure":50,
"alarm_pressure":58,

"vibration":(1,5),
"warning_vibration":4,
"alarm_vibration":5,

"rpm":[3000,4500,6000,9000],

"power_kw":[55,75,90,110,132,160,200],

"maintenance_days":120,

"inspection_days":30,

"lubrication_days":45,

"expected_life_years":18

},

# ==========================================================
# MOTORS
# ==========================================================

"Motor":{

"temperature":(35,95),
"warning_temperature":85,
"alarm_temperature":95,
"pressure": None,

"warning_pressure": None,

"alarm_pressure": None,

"vibration":(0.5,3),
"warning_vibration":2.5,
"alarm_vibration":3,

"rpm":[1450,2900],

"power_kw":[7.5,15,22,30,37,45,55,75],

"maintenance_days":180,

"inspection_days":30,

"lubrication_days":90,

"expected_life_years":15

},

# ==========================================================
# HEAT EXCHANGERS
# ==========================================================

"Heat Exchanger":{

"temperature":(80,250),
"warning_temperature":220,
"alarm_temperature":245,

"pressure":(3,30),
"warning_pressure":25,
"alarm_pressure":30,

"vibration":None,
"warning_vibration": None,
"alarm_vibration": None,

"rpm":None,

"power_kw":None,

"maintenance_days":365,

"inspection_days":90,

"lubrication_days":None,

"expected_life_years":25

},

# ==========================================================
# VALVES
# ==========================================================

"Valve":{

"temperature":(20,250),
"warning_temperature":220,
"alarm_temperature":245,

"pressure":(2,50),
"warning_pressure":45,
"alarm_pressure":50,

"vibration":None,
"warning_vibration": None,

"alarm_vibration": None,
"rpm":None,

"power_kw":None,

"maintenance_days":365,

"inspection_days":90,

"lubrication_days":180,

"expected_life_years":25

},

# ==========================================================
# BOILERS
# ==========================================================

"Boiler":{

"temperature":(150,350),
"warning_temperature":320,
"alarm_temperature":345,

"pressure":(20,120),
"warning_pressure":100,
"alarm_pressure":118,

"vibration":None,
"warning_vibration": None,

"alarm_vibration": None,
"rpm":None,

"power_kw":None,

"maintenance_days":180,

"inspection_days":30,

"lubrication_days":None,

"expected_life_years":30

},

# ==========================================================
# FURNACES
# ==========================================================

"Furnace":{

"temperature":(300,900),
"warning_temperature":850,
"alarm_temperature":890,

"pressure":(1,10),
"warning_pressure":8,
"alarm_pressure":10,

"vibration":None,
"warning_vibration": None,

"alarm_vibration": None,
"rpm":None,

"power_kw":None,

"maintenance_days":120,

"inspection_days":30,

"lubrication_days":None,

"expected_life_years":30

},

# ==========================================================
# TURBINES
# ==========================================================

"Turbine":{

"temperature":(150,450),
"warning_temperature":420,
"alarm_temperature":445,

"pressure":(20,100),
"warning_pressure":90,
"alarm_pressure":98,

"vibration":(0.5,4),
"warning_vibration":3.5,
"alarm_vibration":4,

"rpm":[3000,6000],

"power_kw":[500,750,1000,1500],

"maintenance_days":120,

"inspection_days":30,

"lubrication_days":45,

"expected_life_years":25

},

# ==========================================================
# REACTORS
# ==========================================================

"Reactor":{

"temperature":(180,450),
"warning_temperature":420,
"alarm_temperature":445,

"pressure":(20,80),
"warning_pressure":70,
"alarm_pressure":78,

"vibration":None,
"warning_vibration": None,

"alarm_vibration": None,
"rpm":None,

"power_kw":None,

"maintenance_days":365,

"inspection_days":60,

"lubrication_days":None,

"expected_life_years":30

},

# ==========================================================
# DISTILLATION COLUMNS
# ==========================================================

"Distillation Column":{

"temperature":(120,350),
"warning_temperature":320,
"alarm_temperature":345,

"pressure":(1,8),
"warning_pressure":7,
"alarm_pressure":8,

"vibration":None,
"warning_vibration": None,

"alarm_vibration": None,
"rpm":None,

"power_kw":None,

"maintenance_days":365,

"inspection_days":90,

"lubrication_days":None,

"expected_life_years":30

},

# ==========================================================
# STORAGE TANK
# ==========================================================

"Storage Tank":{

"temperature":(20,90),
"warning_temperature":80,
"alarm_temperature":88,

"pressure":(0,5),
"warning_pressure":4,
"alarm_pressure":5,

"vibration":None,
"warning_vibration": None,

"alarm_vibration": None,
"rpm":None,

"power_kw":None,

"maintenance_days":365,

"inspection_days":180,

"lubrication_days":None,

"expected_life_years":40

},

# ==========================================================
# COOLING SYSTEM
# ==========================================================

"Cooling System":{

"temperature":(15,60),
"warning_temperature":55,
"alarm_temperature":60,

"pressure":(2,10),
"warning_pressure":8,
"alarm_pressure":10,

"vibration":(0.5,2),
"warning_vibration":1.8,
"alarm_vibration":2,

"rpm":[960,1450],

"power_kw":[15,22,30,45],

"maintenance_days":180,

"inspection_days":30,

"lubrication_days":60,

"expected_life_years":20

},

# ==========================================================
# GENERATOR
# ==========================================================

"Generator":{

"temperature":(35,110),
"warning_temperature":100,
"alarm_temperature":108,

"pressure":None,
"warning_pressure": None,

"alarm_pressure": None,
"vibration":(0.5,2.5),
"warning_vibration":2,
"alarm_vibration":2.5,

"rpm":[1500,3000],

"power_kw":[250,500,750,1000],

"maintenance_days":180,

"inspection_days":30,

"lubrication_days":60,

"expected_life_years":25

},

# ==========================================================
# PIPELINE
# ==========================================================

"Pipeline":{

"temperature":(20,180),
"warning_temperature":165,
"alarm_temperature":178,

"pressure":(5,60),
"warning_pressure":55,
"alarm_pressure":60,

"vibration":None,
"warning_vibration": None,

"alarm_vibration": None,
"rpm":None,

"power_kw":None,

"maintenance_days":365,

"inspection_days":180,

"lubrication_days":None,

"expected_life_years":35

},

# ==========================================================
# INSTRUMENTATION
# ==========================================================

"Instrumentation":{

"temperature":(0,120),
"warning_temperature":110,
"alarm_temperature":118,

"pressure":(0,40),
"warning_pressure":35,
"alarm_pressure":40,

"vibration":None,
"warning_vibration": None,

"alarm_vibration": None,
"rpm":None,

"power_kw":None,

"maintenance_days":90,

"inspection_days":30,

"lubrication_days":None,

"expected_life_years":12

}

}