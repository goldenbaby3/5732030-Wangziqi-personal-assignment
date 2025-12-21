import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict
import math

def visualize_related_items(graph, target_items, top_n=20, min_weight=1, save_path=None):
    if isinstance(target_items, str):
        target_items = [target_items.lower()]
    else:
        target_items = [t.lower() for t in target_items]

    H = nx.Graph()

    # Add the products most strongly associated with the target products to the graph.
    for item in target_items:
        if item not in graph:
            continue
        neighbors = sorted(graph[item].items(), key=lambda x: x[1], reverse=True)[:top_n]
        for neighbor, weight in neighbors:
            if weight >= min_weight:
                H.add_edge(item, neighbor, weight=weight)

    if len(H.nodes) == 0:
        print("No products meeting the criteria will be visualized.")
        return

    # spring_layout
    pos = nx.spring_layout(H, k=0.5, iterations=200, seed=42)

    # Adjust the node size and color.
    node_sizes = []
    node_colors = []
    for n in H.nodes():
        base_size = 800 + math.sqrt(H.degree(n)) * 300 
        if n in target_items:
            node_sizes.append(base_size * 2.5)  # Make the central node larger.
            node_colors.append('lightcoral')
        else:
            node_sizes.append(base_size)
            node_colors.append('lightgray')

    edge_weights = [math.log(d['weight'] + 1) for u, v, d in H.edges(data=True)]
    max_weight = max(edge_weights) if edge_weights else 1
    widths = [w / max_weight * 4 for w in edge_weights]

    # Draw the graph
    plt.figure(figsize=(14, 10))
    nx.draw_networkx_nodes(H, pos, node_size=node_sizes, node_color=node_colors,
                           edgecolors='black', linewidths=1.2)
    nx.draw_networkx_edges(H, pos, width=widths, alpha=0.6, edge_color='gray')

    # Add labels
    labels = {n: n for n in H.nodes()}
    nx.draw_networkx_labels(H, pos, labels, font_size=12, font_weight='bold', font_family='SimHei')

    plt.axis('off')
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"图保存到 {save_path}")
    else:
        plt.show()
