import pandas as pd

def load_alagoas_data(file_path):
    """Loads the Alagoas voter profile data."""
    df = pd.read_csv(file_path, sep=';', encoding='ISO-8859-1')
    return df

def load_tte_data(file_path):
    """Loads the TTE voter data."""
    df = pd.read_csv(file_path, encoding='latin1', sep=';')
    return df
