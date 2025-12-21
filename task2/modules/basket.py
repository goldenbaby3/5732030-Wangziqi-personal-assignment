# modules/basket.py
def generate_baskets(df):
    """
    Generate a transaction basket list based on membernumber and date.
    """
    grouped = df.groupby(['Member_number', 'Date'])['itemDescription'].agg(lambda x: list(set(x)))
    return grouped.tolist()
