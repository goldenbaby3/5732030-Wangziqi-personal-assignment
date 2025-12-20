import pytest
import pandas as pd
from modules.visualization import plot_time_trend

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

def test_plot_time_trend(sample_df):
    result = plot_time_trend(sample_df, region='RegionA')
    assert result is not None
    assert 'Month' in result.columns
