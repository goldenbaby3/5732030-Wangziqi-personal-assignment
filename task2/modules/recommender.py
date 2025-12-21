# modules/recommender.py
from collections import defaultdict

def recommend_items(graph, target_items, top_n=10, min_weight=1):
    """
    Given a target product list, recommend the products most likely to be purchased together.
    """
    if isinstance(target_items, str):
        target_items = [target_items.lower()]
    else:
        target_items = [t.lower() for t in target_items]

    scores = defaultdict(int)
    for item in target_items:
        if item not in graph:
            continue
        for neighbor, weight in graph[item].items():
            if neighbor in target_items or weight < min_weight:
                continue
            scores[neighbor] += weight

    recommended = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:top_n]
    return recommended
