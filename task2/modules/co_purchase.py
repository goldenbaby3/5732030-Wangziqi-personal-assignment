# modules/co_purchase.py
def most_common_co_purchased(graph, item, top_n=5):
    """
    Return a list of products most frequently purchased together with the target product.
    """
    item = item.lower()
    if item not in graph:
        return []
    return sorted(graph[item].items(), key=lambda x: x[1], reverse=True)[:top_n]

def are_items_frequently_co_purchased(graph, item1, item2, threshold=5):
    """
    Determine whether two products are frequently purchased together.
    """
    return graph.get(item1.lower(), {}).get(item2.lower(), 0) >= threshold
