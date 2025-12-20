import pytest
import pandas as pd
from modules.filtering import filter_data

@pytest.fixture
def sample_df():
    data = {
        'Local Electoral Area': ['RegionA', 'RegionB'],
        'Statistic Label': ['Vaccinated', 'Vaccinated'],
        'Age Group': ['18-30', '18-30'],
        'VALUE': [10, 20],
        'Month': pd.to_datetime(['2021-01-01', '2021-02-01'])
    }
    return pd.DataFrame(data)

def test_filter_data_region(sample_df):
    df_filtered = filter_data(sample_df, region='RegionA')
    assert len(df_filtered) == 1
    assert df_filtered.iloc[0]['Local Electoral Area'] == 'RegionA'
