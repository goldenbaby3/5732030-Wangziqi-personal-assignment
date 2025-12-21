import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
from modules.filtering import filter_data
import logging

def plot_time_trend(df, region=None, statistic_label=None, age_group=None):
    df_filtered = filter_data(df, region, statistic_label, age_group)
    df_filtered = df_filtered.dropna(subset=['VALUE', 'Month'])
    if df_filtered.empty:
        logging.warning("No data for the selected criteria")
        return None
    df_grouped = df_filtered.groupby('Month')['VALUE'].mean().reset_index()
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    plt.plot(df_grouped['Month'], df_grouped['VALUE'], marker='o', linestyle='-', color='b')
    plt.title(f'Time Trend - {region or "All"} | {statistic_label or "All"} | {age_group or "All"}')
    plt.xlabel('Month')
    plt.ylabel('VALUE')
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    logging.info("Time trend plotted")
    return df_grouped
