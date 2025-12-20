from collections import defaultdict, Counter
from modules.recommender import recommend_items

def mock_graph():
    g = defaultdict(Counter)
    g["bread"]["milk"] = 10
    g["bread"]["eggs"] = 4
    g["milk"]["butter"] = 6
    return g

def test_recommend_items_single():
    graph = mock_graph()
    result = recommend_items(graph, "bread", top_n=1)
    assert result[0][0] == "milk"

def test_recommend_items_multiple():
    graph = mock_graph()
    result = recommend_items(graph, ["bread", "milk"])
    items = [r[0] for r in result]
    assert "butter" in items

def test_recommend_items_unknown():
    graph = mock_graph()
    result = recommend_items(graph, "unknown")
    assert result == []
