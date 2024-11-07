import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import requests
import googlemaps
from haversine import haversine ,Unit

API='################'
gmaps=googlemaps.Client(key=API)

def geocode_addresses(addresses):
    """Geocodes a list of addresses.
    Args:
        addresses (list): List of addresses to geocode.
    Returns:
        pd.DataFrame: DataFrame with address, latitude, and longitude.
    """
    results = []
    for address in addresses:
        
        geocode_result = gmaps.geocode(address)
        if geocode_result:
            location = geocode_result[0]['geometry']['location']
            lat, lng = location['lat'], location['lng']
            results.append({
                'address': address,
                'latitude': lat,
                'longitude': lng
            })
            print(f"Geocoded: {address} -> Latitude: {lat}, Longitude: {lng}")
        else:
            results.append({
                'address': address,
                'latitude': None,
                'longitude': None
            })
            print(f"Geocoding failed for: {address}")
                
            # Optional: delay to respect rate limits
            time.sleep(0.1)  # Adjust based on your quota and needs
    
    # Convert results to a DataFrame for easy manipulation
    return pd.DataFrame(results)


#Input
sum_air=['Beijing Capital International Airport','Shanghai Pudong International Airport']
num_air={'Beijing Capital International Airport':10,'Shanghai Pudong International Airport':5}
emission_factor_air=0.255

singapore_air=geocode_addresses(['Singapore Changi Airport'])
foreign_air_location=geocode_addresses(sum_air)
foreign_air_location


distance_air=[0]*len(foreign_air_location)
for i in range(len(foreign_air_location)):
    distance_air[i] = haversine(singapore_air.iloc[0][['latitude','longitude']], foreign_air_location.iloc[i][['latitude','longitude']])  # Example coordinates for Singapore Changi Airport 
distance_air
#this is 'kilometer'

sum_distance=[0]*len(distance_air)
for i in range(len(distance_air)):
    sum_distance[i]=distance_air[i]*num_air[sum_air[i]]
sum_distance

sum_distance=np.array(sum_distance)
emission_air=sum_distance*emission_factor_air
emission_air

print(emission_air.sum())