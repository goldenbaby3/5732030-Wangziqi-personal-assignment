# modules/frequent_items.py
from collections import Counter
from itertools import combinations

def frequent_itemsets(transactions, k=2, top_n=3):
    """
    Return the top k most frequent product combinations.
    """
    counter = Counter()
    for basket in transactions:
        for combo in combinations(sorted(basket), k):
            counter[combo] += 1
    return counter.most_common(top_n)
