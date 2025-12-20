import pytest
import pandas as pd
from modules.data_io import clean_data, load_data, export_to_csv

@pytest.fixture
def sample_df():
    data = {'Month': ['2021-01', '2021-02', 'invalid'], 'VALUE': ['10', '20', 'NaN']}
    return pd.DataFrame(data)

def test_clean_data(sample_df):
    df_clean = clean_data(sample_df)
    assert len(df_clean) == 2
    assert pd.api.types.is_datetime64_any_dtype(df_clean['Month'])
    assert pd.api.types.is_float_dtype(df_clean['VALUE'])
