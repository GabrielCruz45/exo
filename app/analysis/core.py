# Functions for data cleaning, ESI calculation, stats, etc.
import pandas as pd
import logging
import math

# filePath = '../../data/exp.csv'


def load_exoplanet_data(filepath: str) -> pd.DataFrame:
    
    required_columns = [
        'pl_name', 'hostname', 'discoverymethod', 'pl_rade', 
        'pl_bmasse', 'pl_eqt', 'pl_orbper', 'st_teff'
        ]
    
    # create and add to data Frame new column with esi value for each planet .apply()
    
    try:
        dataFrame = pd.read_csv(filepath, comment='#', usecols=required_columns).dropna()
        dataFrame['ESI'] = dataFrame.apply(calculate_esi, axis=1)
        return dataFrame
    
    except FileNotFoundError:
        logging.error(f"Error: The file at {filepath} was not found.")
        return pd.DataFrame()
    
    except ValueError as e:
        logging.error(f"Error reading columns from {filepath}: {e}")
        return pd.DataFrame()
    


def calculate_esi(planet_data): # takes single planet's data as a Pandas Series or Python dictionary
    
    # ESI SI units
    # temperature SI unit -> K
    # mass SI unit -> kg
    # radius SI unit -> m
    # bulk density SI unit -> g/cm^3

    # universal gravitational constant; SI units -> (m^3⋅kg^−1⋅s^−2)
    G = 6.6743e-11

    # earth values
    ST_EARTH = 288
    R_EARTH = 6371000
    MK_EARTH = 5.972e24 # mass in kilograms
    BD_EARTH = 5.51 
    EV_EARTH = math.sqrt((2 * MK_EARTH * G) / R_EARTH)


    # parse through planet's data
    st_planet = planet_data['pl_eqt']
    r_planet = planet_data['pl_rade'] * R_EARTH # radius in meters
    mK_planet = planet_data['pl_bmasse'] * MK_EARTH

    # calculates planet's bulk density; then corrects units to g/cm^3 (divide by 1000)
    bd_planet = ((mK_planet / ((4/3) * math.pi * (r_planet) ** 3)) / 1000) 
    ev_planet = math.sqrt((2 * mK_planet * G) / r_planet)


    # esi constants
    ST_WEIGHT = 5.80
    BD_WEIGHT = 1.07
    EV_WEIGHT = 0.70
    R_WEIGHT = 0.57


    # sponge me boy, run ESI formular
    surface_temperature = (1 - abs((st_planet - ST_EARTH) / (st_planet + ST_EARTH))) ** (ST_WEIGHT)
    bulk_density = (1 - abs((bd_planet - BD_EARTH) / (bd_planet + BD_EARTH))) ** (BD_WEIGHT)
    escape_velocity = (1 - abs((ev_planet - EV_EARTH) / (ev_planet + EV_EARTH))) ** (EV_WEIGHT)
    radius = (1 - abs((r_planet - R_EARTH) / (r_planet + R_EARTH))) ** (R_WEIGHT)


    try:
        # calculate final ESI value
        return (surface_temperature * bulk_density * escape_velocity * radius) ** (1/4)
    
    except Exception as e:
        logging.error(f"Could not calculate ESI for a planet: {e}")
        return math.nan
