import logging

def display_summary(df):
    summary = df.describe()
    logging.info("Displayed statistical summary")
    return summary

def group_by_region(df):
    grouped = df.groupby('Local Electoral Area')['VALUE'].agg(['mean','std','min','max','count']).reset_index()
    logging.info("Grouped by region")
    return grouped

def group_by_date(df):
    temp_df = df.copy()
    temp_df['Year-Month'] = temp_df['Month'].dt.to_period('M').astype(str)
    grouped = temp_df.groupby('Year-Month')['VALUE'].agg(['mean','std','min','max','count']).reset_index()
    logging.info("Grouped by Year-Month")
    return grouped
