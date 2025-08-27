import pandas as pd

def clean_and_process_alagoas_data(df):
    """Cleans and processes the Alagoas voter profile data."""
    df.replace({'#NULO': None, '#NE': None, -1: None, -3: None}, inplace=True)
    numeric_cols = ['QT_APTOS', 'QT_COMPARECIMENTO', 'QT_ABSTENCAO']
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')
    df['PCT_COMPARECIMENTO'] = (df['QT_COMPARECIMENTO'] / df['QT_APTOS']) * 100
    df['PCT_ABSTENCAO'] = (df['QT_ABSTENCAO'] / df['QT_APTOS']) * 100
    return df

def clean_and_process_tte_data(df):
    """Cleans and processes the TTE voter data."""
    df["QT_APTOS_EM_TTE"] = pd.to_numeric(df["QT_APTOS_EM_TTE"], errors="coerce")
    df["QT_COMPARECIMENTO_TTE"] = pd.to_numeric(df["QT_COMPARECIMENTO_TTE"], errors="coerce")
    df["QT_ABSTENCAO_TTE"] = pd.to_numeric(df["QT_ABSTENCAO_TTE"], errors="coerce")
    return df

def calculate_disability_percentages(df):
    """Calculates percentages for voters with disabilities."""
    numeric_cols = ['QT_APTOS', 'QT_COMPARECIMENTO', 'QT_ABSTENCAO', 'QT_COMPARECIMENTO_DEFICIENCIA', 'QT_ABSTENCAO_DEFICIENCIA']
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')
    df['PCT_COMPARECIMENTO_DEFICIENCIA'] = (df['QT_COMPARECIMENTO_DEFICIENCIA'] / df['QT_APTOS']) * 100
    df['PCT_ABSTENCAO_DEFICIENCIA'] = (df['QT_ABSTENCAO_DEFICIENCIA'] / df['QT_APTOS']) * 100
    return df
