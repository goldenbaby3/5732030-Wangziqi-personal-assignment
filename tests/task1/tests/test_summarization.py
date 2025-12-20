import pytest
import pandas as pd
from modules.summarization import display_summary, group_by_region, group_by_date

@pytest.fixture
def sample_df():
    data = {
        'Local Electoral Area': ['RegionA', 'RegionB'],
        'VALUE': [10, 20],
        'Month': pd.to_datetime(['2021-01-01', '2021-02-01'])
    }
    return pd.DataFrame(data)

def test_display_summary(sample_df):
    summary = display_summary(sample_df)
    assert 'VALUE' in summary.columns

def test_group_by_region(sample_df):
    grouped = group_by_region(sample_df)
    assert 'mean' in grouped.columns

def test_group_by_date(sample_df):
    grouped = group_by_date(sample_df)
    assert 'Year-Month' in grouped.columns
