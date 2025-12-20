from collections import defaultdict, Counter
from modules.co_purchase import (
    most_common_co_purchased,
    are_items_frequently_co_purchased
)

def mock_graph():
    g = defaultdict(Counter)
    g["bread"]["milk"] = 10
    g["bread"]["eggs"] = 3
    return g

def test_most_common_co_purchased():
    graph = mock_graph()
    result = most_common_co_purchased(graph, "bread", top_n=1)
    assert result[0][0] == "milk"

def test_are_items_frequently_co_purchased_true():
    graph = mock_graph()
    assert are_items_frequently_co_purchased(graph, "bread", "milk", threshold=5)

def test_are_items_frequently_co_purchased_false():
    graph = mock_graph()
    assert not are_items_frequently_co_purchased(graph, "bread", "eggs", threshold=5)
