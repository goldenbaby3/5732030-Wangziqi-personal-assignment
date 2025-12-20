import pandas as pd
from modules.basket import generate_baskets

def test_generate_baskets_basic():
    df = pd.DataFrame({
        "Member_number": [1, 1, 2],
        "Date": ["2023-01-01", "2023-01-01", "2023-01-02"],
        "itemDescription": ["bread", "milk", "eggs"]
    })

    baskets = list(generate_baskets(df))
    assert len(baskets) == 2
    assert set(baskets[0]) == {"bread", "milk"}

def test_generate_baskets_empty():
    df = pd.DataFrame(columns=["Member_number", "Date", "itemDescription"])
    baskets = list(generate_baskets(df))
    assert baskets == []
