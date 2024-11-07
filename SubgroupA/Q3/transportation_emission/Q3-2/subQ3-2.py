import googlemaps
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import requests


API='AIzaSyCcsxYeAZosGeKlXZmUNF1bWNXwQ7MPU3g'
gmaps=googlemaps.Client(key=API)

#Input
addresses = [
    "126752",
    "Changi Airport, Singapore",
    "Singapore Zoo, Singapore",
    "Gardens by the Bay, Singapore",
    "NUS, Singapore"
]
mode_commute={"126752": 'driving',
    "Changi Airport, Singapore": 'walking',
    "Singapore Zoo, Singapore": 'bicycling',
    "Gardens by the Bay, Singapore": 'transit',
    "NUS, Singapore":'driving'}
destination='126752'
travel_modes=['driving', 'walking', 'transit','bicycling']
mode_emission_factor={'driving':0.00017, 'walking':0.00, 'transit':0.00007,'bicycling':0.0000001}

def calculate_distances(addresses, destination, travel_modes):
    """Calculates distance and time from multiple origins to a single destination for specified travel modes.
    Args:
        origins (list): List of origin addresses or latitude, longitude pairs.
        destination (str): Destination address or latitude, longitude pair.
        travel_modes (list): List of travel modes (e.g., 'driving', 'walking', 'transit').
    Returns:
        pd.DataFrame: DataFrame with distances and durations for each mode.
    """
    results = []
    for origin in addresses:
        for mode in travel_modes:
            try:
                # Get the distance matrix for the specified mode
                response = gmaps.distance_matrix(origin, destination, mode=mode)

                if response['rows']:
                    element = response['rows'][0]['elements'][0]
                    distance_text = element.get('distance', {}).get('text', 'N/A')
                    duration_text = element.get('duration', {}).get('text', 'N/A')
                    distance_value = element.get('distance', {}).get('value', 0)  # Distance in meters
                    duration_value = element.get('duration', {}).get('value', 0)  # Duration in seconds

                    # Append the result for this origin, mode, and destination
                    results.append({
                        'origin': origin,
                        'destination': destination,
                        'mode': mode,
                        
                        'distance_meters': distance_value,
                        
                        'duration_seconds': duration_value
                    })
                    print(f"Origin: {origin}, Mode: {mode}")
                
                # Delay to respect rate limits
                time.sleep(0.1)
            
            except Exception as e:
                print(f"Error calculating distance from {origin} using mode {mode}: {e}")

    # Convert results to a DataFrame for easier analysis
    return pd.DataFrame(results)

distance_results = calculate_distances(addresses, destination,travel_modes)
distance_results.to_csv('commuting_distances.csv', index=False)

distance_results['emission_factor']=0.001

for i in distance_results['mode']:
    distance_results.loc[distance_results['mode']==i,'emission_factor']=mode_emission_factor[i]

distance_results['emission']=distance_results['emission_factor']*distance_results['distance_meters']

max_emission=distance_results.groupby('origin')['emission'].max().sum()
min_emission=distance_results.groupby('origin')['emission'].min().sum()
print(max_emission,min_emission)

#with exact commuting way
start = 0.00
# Iterate over unique origins
for i in distance_results['origin'].unique():
    # Get the mode for the origin from mode_pattern, defaulting to None if not found
    mode = mode_commute.get(i)
    
    # Proceed if a mode is found for the origin
    if mode:
        # Filter the DataFrame for the current origin and the corresponding mode
        filtered_emission = distance_results[
            (distance_results['origin'] == i) & 
            (distance_results['mode'] == mode)
        ]['emission'].sum()  # Use .sum() to sum the 'emission' values

        # Add the summed emissions to the total start value
        start += filtered_emission

print(f"Total Emission: {start}")