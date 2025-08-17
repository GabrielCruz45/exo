# Functions for data cleaning, ESI calculation, stats, etc.
import pandas as pd
import logging

# filePath = '../../data/exp.csv'

def load_exoplanet_data(filepath: str) -> pd.DataFrame:
    
    required_columns = [
        'pl_name', 'hostname', 'discoverymethod', 'pl_rade', 
        'pl_bmasse', 'pl_eqt', 'pl_orbper', 'st_teff'
        ]
    
    try:
        dataFrame = pd.read_csv(filepath, comment='#', usecols=required_columns).dropna()
        return dataFrame
    
    except FileNotFoundError:
        logging.error(f"Error: The file at {filepath} was not found.")
        return pd.DataFrame()
    
    except ValueError as e:
        logging.error(f"Error reading columns from {filepath}: {e}")
        return pd.DataFrame()
