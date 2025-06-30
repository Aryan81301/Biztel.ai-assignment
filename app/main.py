# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.data_loader import DataLoader
from src.cleaner import DataCleaner
from src.analyzer import Analyzer
import pandas as pd

app = FastAPI()
DATA_PATH = "data/BiztelAI_DS_Dataset_V1.json"
data_df = None

@app.on_event("startup")
def load_and_prepare_data():
    global data_df
    data_df = DataLoader(DATA_PATH).load_data()
    data_df = DataCleaner(data_df).clean()

class ChatInput(BaseModel):
    conversation_id: str

@app.get("/summary")
def get_summary():
    return {
        "total_chats": data_df['conversation_id'].nunique(),
        "total_messages": len(data_df),
        "unique_articles": data_df['article_url'].nunique()
    }

@app.post("/analyze_transcript")
def analyze_transcript(input_data: ChatInput):
    chat_df = data_df[data_df['conversation_id'] == input_data.conversation_id]
    if chat_df.empty:
        raise HTTPException(status_code=404, detail="Transcript not found")
    return Analyzer(data_df).summarize_chat(chat_df)

@app.get("/transform")
def get_transformed_text(text: str):
    from src.text_processor import TextProcessor
    return {"transformed": TextProcessor().process_text(text)}