import logging

def filter_data(df, region=None, statistic_label=None, age_group=None):
    df_filtered = df.copy()
    if region and 'Local Electoral Area' in df.columns:
        df_filtered = df_filtered[df_filtered['Local Electoral Area'].str.lower().str.contains(region.lower())]
    if statistic_label and 'Statistic Label' in df.columns:
        df_filtered = df_filtered[df_filtered['Statistic Label'].str.lower().str.contains(statistic_label.lower())]
    if age_group and 'Age Group' in df.columns:
        df_filtered = df_filtered[df_filtered['Age Group'].str.lower().str.contains(age_group.lower())]
    logging.info(f"Filtered data: region={region}, statistic_label={statistic_label}, age_group={age_group}, rows={len(df_filtered)}")
    return df_filtered
