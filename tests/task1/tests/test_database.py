import pytest
import pandas as pd
from modules.database import init_db, save_to_db, read_from_db
import os

@pytest.fixture
def sample_df():
    data = {
        'Month': pd.to_datetime(['2021-01-01', '2021-02-01']),
        'Local Electoral Area': ['RegionA', 'RegionB'],
        'Statistic Label': ['Vaccinated', 'Vaccinated'],
        'Age Group': ['18-30', '18-30'],
        'VALUE': [10, 20]
    }
    return pd.DataFrame(data)

def test_save_and_read_db(tmp_path, sample_df):
    db_file = tmp_path / "test.db"
    conn = init_db(str(db_file))
    save_to_db(sample_df, conn)
    df_read = read_from_db(conn)
    assert len(df_read) == 2
    conn.close()
