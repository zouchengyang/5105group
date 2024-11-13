import pandas as pd

def prepare_data(file_path):
    data = pd.read_csv(file_path)
    features = [
        'Primary Property Type - Self Selected',
        'Largest Property Use Type',
        'Primary Property Use Type - Gross Floor Area (ft²)',
        'Year Built',
        'Number of Buildings - Self-reported',
        'Occupancy',
        'Water Intensity (All Water Sources) (gal/ft²)',
        'age',
        'age_group',
        'Occupancy_group',
        'Latitude',
        'Longitude',
        'Site EUI (kBtu/ft²)',
        'Weather Normalized Site Electricity Intensity (kWh/ft²)',
        'Weather Normalized Site Natural Gas Intensity (therms/ft²)',
        'Water Use (All Water Sources) (kgal)'
    ]
    target = 'GHG Emissions'
    data = data.dropna(subset=[target])
    X = data[features]
    y = data[target]
    return X, y