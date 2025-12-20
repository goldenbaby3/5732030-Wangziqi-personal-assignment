from modules.graph_builder import build_co_purchase_graph

def test_build_graph_basic():
    transactions = [
        ["bread", "milk"],
        ["bread", "eggs"]
    ]

    graph = build_co_purchase_graph(transactions)

    assert graph["bread"]["milk"] == 1
    assert graph["bread"]["eggs"] == 1
    assert graph["milk"]["bread"] == 1

def test_build_graph_empty():
    graph = build_co_purchase_graph([])
    assert len(graph) == 0
