# src/analyzer.py

import pandas as pd  # ✅ This line is required
from collections import Counter

class Analyzer:
    def init__(self, df: pd.DataFrame):  # Note: use __init, not init
        self.df = df

    def summarize_chat(self, chat_df: pd.DataFrame) -> dict:
        agent1_msgs = chat_df[chat_df['agent'] == 'agent_1']
        agent2_msgs = chat_df[chat_df['agent'] == 'agent_2']
        summary = {
            "article_url": chat_df['article_url'].iloc[0],
            "message_count_agent_1": len(agent1_msgs),
            "message_count_agent_2": len(agent2_msgs),
            "agent_1_sentiments": dict(Counter(agent1_msgs['sentiment'])),
            "agent_2_sentiments": dict(Counter(agent2_msgs['sentiment']))
        }
        return summary
