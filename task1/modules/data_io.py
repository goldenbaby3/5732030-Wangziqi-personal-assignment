import pandas as pd
import logging

logging.basicConfig(filename='dashboard.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        logging.info(f"Loaded data from {file_path}")
        return df
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return None

def clean_data(df):
    df['Month'] = pd.to_datetime(df['Month'], errors='coerce')
    df['VALUE'] = pd.to_numeric(df['VALUE'], errors='coerce')
    df = df.dropna(subset=['Month', 'VALUE'])
    logging.info(f"Data cleaned: {len(df)} rows remain")
    return df

def export_to_csv(df, file_name):
    df.to_csv(file_name, index=False)
    logging.info(f"Data exported to {file_name}")
