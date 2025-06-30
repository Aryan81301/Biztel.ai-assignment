# src/cleaner.py
import pandas as pd

class DataCleaner:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def clean(self) -> pd.DataFrame:
        df = self.df.dropna(subset=['message', 'agent'])

        # 🔥 Fix: Convert lists to strings for deduplication
        if 'knowledge_source' in df.columns:
            df['knowledge_source'] = df['knowledge_source'].apply(lambda x: ','.join(x) if isinstance(x, list) else str(x))

        df = df.drop_duplicates()
        df['message'] = df['message'].str.strip()
        df['sentiment'] = df['sentiment'].fillna("Unknown")
        return df
