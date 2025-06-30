# data_loader.py
import json
import pandas as pd

class DataLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_data(self) -> pd.DataFrame:
        with open(self.file_path, 'r') as f:
            raw_data = json.load(f)

        records = []
        for conv_id, conv_data in raw_data.items():
            article_url = conv_data.get("article_url", "")
            conversation = conv_data.get("content", [])
            for msg in conversation:
                records.append({
                    "conversation_id": conv_id,
                    "article_url": article_url,
                    "message": msg.get("message", ""),
                    "agent": msg.get("agent", ""),
                    "sentiment": msg.get("sentiment", ""),
                    "knowledge_source": msg.get("knowledge_source", []),
                    "turn_rating": msg.get("turn_rating", "")
                })
        return pd.DataFrame(records)