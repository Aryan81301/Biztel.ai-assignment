#cleaner.py
import pandas as pd

class DataCleaner:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def clean(self) -> pd.DataFrame:
        df = self.df.dropna(subset=['message', 'agent'])
        df = df.drop_duplicates()
        df['message'] = df['message'].str.strip()
        df['sentiment'] = df['sentiment'].fillna("Unknown")
        return df