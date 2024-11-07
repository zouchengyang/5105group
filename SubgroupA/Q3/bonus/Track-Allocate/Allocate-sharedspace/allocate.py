import pandas as pd

building_type_total=['Office Building','Residential Complex','Retail Center']

# Data for each building type with their total emissions, tenant breakdown, and specific emission factors
buildings_data = [
    {
        "building_type": "Office Building",
        "total_emissions_kgCO2e": 12000,
        "tenants": [
            {"tenant_type": "Office Tenant A", "area_percentage": 40, "emission_factor": 0.7},
            {"tenant_type": "Office Tenant B", "area_percentage": 35, "emission_factor": 0.8},
            {"tenant_type": "Cafeteria", "area_percentage": 25, "emission_factor": 1.8},
        ],
    },
    {
        "building_type": "Residential Complex",
        "total_emissions_kgCO2e": 8000,
        "tenants": [
            {"tenant_type": "Residential Tenant A", "area_percentage": 50, "emission_factor": 0.9},
            {"tenant_type": "Residential Tenant B", "area_percentage": 30, "emission_factor": 1.0},
            {"tenant_type": "Residential Tenant C", "area_percentage": 20, "emission_factor": 0.85},
        ],
    },
    {
        "building_type": "Retail Center",
        "total_emissions_kgCO2e": 15000,
        "tenants": [
            {"tenant_type": "Retail Shop A", "area_percentage": 30, "emission_factor": 0.5},
            {"tenant_type": "Retail Shop B", "area_percentage": 40, "emission_factor": 0.6},
            {"tenant_type": "Food Court", "area_percentage": 30, "emission_factor": 1.5},
        ],
    },
]

# Calculate emissions allocation for each building and tenant, considering their emission factor
emission_allocation_results = []

for building in buildings_data:
    building_type = building["building_type"]
    total_emissions = building["total_emissions_kgCO2e"]

    # Calculate total weighted factor for all tenants to properly allocate emissions
    total_weighted_factor = sum(
        (tenant["area_percentage"] / 100) * tenant["emission_factor"] for tenant in building["tenants"]
    )

    for tenant in building["tenants"]:
        tenant_type = tenant["tenant_type"]
        area_percentage = tenant["area_percentage"]
        emission_factor = tenant["emission_factor"]

        # Calculate the proportion of emissions based on area percentage and emission factor
        weighted_share = (area_percentage / 100) * emission_factor
        tenant_emission_allocation = (weighted_share / total_weighted_factor) * total_emissions

        # Append the result to the list
        emission_allocation_results.append(
            {
                "building_type": building_type,
                "tenant_type": tenant_type,
                "area_percentage": area_percentage,
                "emission_factor": emission_factor,
                "emission_allocation_kgCO2e": tenant_emission_allocation,
            }
        )

# Create a DataFrame for better visualization and analysis
df = pd.DataFrame(emission_allocation_results)

# Display the resulting DataFrame
print(df)