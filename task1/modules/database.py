import sqlite3
import logging
import pandas as pd

def init_db(db_name='dashboard.db'):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS vaccination_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Month TEXT,
            Local_Electoral_Area TEXT,
            Statistic_Label TEXT,
            Age_Group TEXT,
            VALUE REAL
        )
    ''')
    conn.commit()
    return conn

def save_to_db(df, conn):
    df.to_sql('vaccination_data', conn, if_exists='replace', index=False)
    logging.info("Data saved to database")

def read_from_db(conn):
    df = pd.read_sql_query("SELECT * FROM vaccination_data", conn)
    logging.info("Read data from database")
    return df
