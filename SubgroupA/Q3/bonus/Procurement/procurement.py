import pandas as pd

# Emission factors (kg CO2 per km)
EMISSION_FACTORS = {
    "car": 0.2,
    "bus": 0.1,
    "train": 0.05,
    "bike": 0.0,  # Assuming no emissions for bikes
    "walking": 0.0  # Assuming no emissions for walking
}

# Example employee commuting data
employee_data = [
    {"employee_id": "E001", "mode_of_transport": "car", "distance_km": 15, "frequency_per_week": 5},
    {"employee_id": "E002", "mode_of_transport": "bus", "distance_km": 10, "frequency_per_week": 5},
    {"employee_id": "E003", "mode_of_transport": "train", "distance_km": 20, "frequency_per_week": 3},
    {"employee_id": "E004", "mode_of_transport": "bike", "distance_km": 5, "frequency_per_week": 5},
]

# Calculate emissions for each employee
employee_emissions = []
for employee in employee_data:
    emission_factor = EMISSION_FACTORS.get(employee["mode_of_transport"], 0)
    weekly_emissions = employee["distance_km"] * employee["frequency_per_week"] * emission_factor
    employee_emissions.append({
        "employee_id": employee["employee_id"],
        "mode_of_transport": employee["mode_of_transport"],
        "weekly_emission_kgCO2e": weekly_emissions
    })

# Convert to DataFrame for easier analysis
df_employee_emissions = pd.DataFrame(employee_emissions)
print(df_employee_emissions)
