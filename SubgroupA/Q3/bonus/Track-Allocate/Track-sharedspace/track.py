import pandas as pd

class Tenant:
    def __init__(self, tenant_id, name, area, occupants, tenant_type, emission_factor):
        self.tenant_id = tenant_id
        self.name = name
        self.area = area  # in square meters
        self.occupants = occupants  # number of occupants
        self.tenant_type = tenant_type
        self.emission_factor = emission_factor  # emission factor specific to tenant type

    def __repr__(self):
        return f"Tenant({self.tenant_id}, {self.name}, Type: {self.tenant_type}, Area: {self.area}m², Occupants: {self.occupants}, Emission Factor: {self.emission_factor})"


class Building:
    def __init__(self, building_name):
        self.building_name = building_name
        self.tenants = []
        self.shared_emissions_data = pd.DataFrame(columns=["month", "emission_type", "emission_value_kgCO2e"])
        self.tenant_emissions_data = pd.DataFrame(columns=["tenant_id", "month", "emission_type", "emission_value_kgCO2e"])

    def add_tenant(self, tenant):
        self.tenants.append(tenant)

    def record_shared_emission(self, month, emission_type, emission_value_kgCO2e):
        """Records emission data for shared spaces for a given month"""
        data = {
            "month": month,
            "emission_type": emission_type,
            "emission_value_kgCO2e": emission_value_kgCO2e
        }
        self.shared_emissions_data = pd.concat([self.shared_emissions_data, pd.DataFrame([data])], ignore_index=True)

    def allocate_shared_emissions(self, month):
        """Allocate shared emissions to tenants based on both area and occupants"""
        # Filter shared emissions for the given month
        shared_emissions = self.shared_emissions_data[self.shared_emissions_data["month"] == month]

        # Calculate the total weighted factor based on area, occupants, and emission factor
        total_weighted_factor = sum(
            (tenant.area * tenant.occupants * tenant.emission_factor) for tenant in self.tenants
        )

        for _, row in shared_emissions.iterrows():
            for tenant in self.tenants:
                weighted_share = tenant.area * tenant.occupants * tenant.emission_factor
                tenant_emission_allocation = (weighted_share / total_weighted_factor) * row["emission_value_kgCO2e"]
                self.record_tenant_emission(tenant.tenant_id, month, row["emission_type"], tenant_emission_allocation)

    def record_tenant_emission(self, tenant_id, month, emission_type, emission_value_kgCO2e):
        """Records emission data for a specific tenant"""
        data = {
            "tenant_id": tenant_id,
            "month": month,
            "emission_type": emission_type,
            "emission_value_kgCO2e": emission_value_kgCO2e
        }
        self.tenant_emissions_data = pd.concat([self.tenant_emissions_data, pd.DataFrame([data])], ignore_index=True)

    def generate_report(self):
        """Generates a summary report by tenant"""
        report = self.tenant_emissions_data.groupby("tenant_id").sum().drop(columns=["month"])
        return report

# Example Usage
# Create Building
building = Building("Multi-Tenant Office")

# Add Tenants with different emission factors
tenant1 = Tenant("T001", "Office Tenant A", area=150, occupants=10, tenant_type="Office", emission_factor=1.2)
tenant2 = Tenant("T002", "Cafeteria B", area=100, occupants=5, tenant_type="Cafeteria", emission_factor=0.8)
tenant3 = Tenant("T003", "Retail Tenant C", area=200, occupants=20, tenant_type="Retail", emission_factor=1.0)

building.add_tenant(tenant1)
building.add_tenant(tenant2)
building.add_tenant(tenant3)

# Record Shared Emissions (e.g., emissions from central heating, shared lights)
building.record_shared_emission("August", "electricity", 1000)
building.record_shared_emission("August", "water", 500)

# Allocate shared emissions among tenants considering area, occupants, and emission factors
building.allocate_shared_emissions("August")

# Generate and view the report
report = building.generate_report()
print(report)