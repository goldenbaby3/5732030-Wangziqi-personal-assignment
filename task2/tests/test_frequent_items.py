from modules.frequent_items import frequent_itemsets

def test_frequent_itemsets_basic():
    transactions = [
        ["bread", "milk"],
        ["bread", "milk"],
        ["bread", "eggs"]
    ]

    result = frequent_itemsets(transactions, k=2, top_n=1)
    assert result[0][0] == ("bread", "milk")
    assert result[0][1] == 2

def test_frequent_itemsets_empty():
    result = frequent_itemsets([], k=2)
    assert result == []
