# run_system2.py
import os
import pandas as pd

# Import modular features (package import)
from modules.basket import generate_baskets
from modules.graph_builder import build_co_purchase_graph
from modules.co_purchase import most_common_co_purchased, are_items_frequently_co_purchased
from modules.frequent_items import frequent_itemsets
from modules.recommender import recommend_items
from modules.visualizer import visualize_related_items

# CSV file path
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'data', 'Supermarket_dataset_PAI.csv')
if not os.path.isfile(file_path):
    raise FileNotFoundError(f"CSV file does not exist: {file_path}")

# Read CSV
df = pd.read_csv(file_path, sep=',', encoding='utf-8-sig')
df.columns = df.columns.str.strip()
df['itemDescription'] = df['itemDescription'].fillna('').str.strip().str.lower()

transactions = generate_baskets(df)
graph = build_co_purchase_graph(transactions)

# Initial analysis
def initial_analysis():
    print("\n=== Initial analysis ===")
    top_items = most_common_co_purchased(graph, 'whole milk', top_n=5)
    print("'whole milk' Most frequently purchased together products:", top_items)

    top_combos = frequent_itemsets(transactions, k=2, top_n=3)
    print("\nMost common two-product combinations:")
    for combo, count in top_combos:
        print(f"{combo[0]} + {combo[1]}: {count} times")

    frequent = are_items_frequently_co_purchased(graph, 'whole milk', 'bread', threshold=5)
    print(f"\nDetermine if 'whole milk' and 'bread' are frequently purchased together (threshold = 5): {frequent}")

# Interactive recommendation system
def run_recommendation_system():
    print("\n=== Small-scale product recommendation system ===")
    user_input = input("Please enter the product(s) (separate multiple products with commas): ").strip()
    if not user_input:
        print("No product entered, exiting.")
        return

    target_items = [x.strip() for x in user_input.split(',') if x.strip()]
    print(f"\nThe product(s) you entered: {target_items}")

    recommendations = recommend_items(graph, target_items, top_n=10, min_weight=5)
    if recommendations:
        print("\nRecommended products and total co-purchase count:")
        for item, score in recommendations:
            print(f"{item}: {score}")
    else:
        print("No recommended products found.")

    save_option = input("Do you want to save the visualization as a PNG file?(y/n): ").strip().lower()
    save_path = None
    if save_option == 'y':
        save_path = input("Please enter the save path, for example data/recommendation.png: ").strip()
    visualize_related_items(graph, target_items, top_n=15, min_weight=5, save_path=save_path)

# Main program entry
if __name__ == "__main__":
    initial_analysis()
    run_recommendation_system()
