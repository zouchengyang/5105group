import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import requests

#input
travel_modes=['driving', 'walking', 'transit','bicycling']
mode_emission_factor={'driving':0.00017, 'walking':0.00, 'transit':0.00007,'bicycling':0.0000001}
mode_distance={'driving':10000, 'walking':5000, 'transit':4000,'bicycling':34500}

#output
total_em=0
for i in travel_modes:
    total_em=total_em+mode_distance[i]*mode_emission_factor[i]
print(total_em)