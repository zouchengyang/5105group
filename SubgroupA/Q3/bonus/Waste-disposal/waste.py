import pandas as pd

# Emission factors (kg CO2e per kg of waste)

WASTE_EMISSION_FACTORS = {
    "plastic": 6.0,
    "paper": 3.0,
    "organic": 1.8,
    "glass": 0.6,
    "metal": 1.2
}

# Example waste disposal data
waste_data = [
    {"waste_type": "plastic", "quantity_kg": 50},
    {"waste_type": "paper", "quantity_kg": 30},
    {"waste_type": "organic", "quantity_kg": 100},
    {"waste_type": "glass", "quantity_kg": 20},
]

# Calculate emissions for each type of waste
waste_emissions = []
for waste in waste_data:
    emission_factor = WASTE_EMISSION_FACTORS.get(waste["waste_type"], 0)
    waste_emission = waste["quantity_kg"] * emission_factor
    waste_emissions.append({
        "waste_type": waste["waste_type"],
        "quantity_kg": waste["quantity_kg"],
        "emission_kgCO2e": waste_emission
    })

df_waste_emissions = pd.DataFrame(waste_emissions)
print(df_waste_emissions)
