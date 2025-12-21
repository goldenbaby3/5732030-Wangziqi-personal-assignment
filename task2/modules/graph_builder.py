# modules/graph_builder.py
from collections import defaultdict, Counter
from itertools import combinations

def build_co_purchase_graph(transactions):
    """
    Construct a product co-purchase graph and return it in the form of an adjacency list.
    """
    pair_counter = Counter()
    for basket in transactions:
        for pair in combinations(sorted(basket), 2):
            pair_counter[pair] += 1

    graph = defaultdict(Counter)
    for (item1, item2), count in pair_counter.items():
        graph[item1][item2] = count
        graph[item2][item1] = count
    return graph
