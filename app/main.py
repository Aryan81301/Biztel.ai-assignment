# app/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.data_loader import DataLoader
from src.cleaner import DataCleaner
from src.analyzer import Analyzer
from src.text_processor import TextProcessor
import pandas as pd
import os

app = FastAPI(title="BiztelAI Chat Transcript Analyzer")

# Set the dataset path from Desktop
DESKTOP = os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop")
DATA_PATH = os.path.join(DESKTOP, "biztel", "data", "BiztelAI_DS_Dataset_V1.json")

data_df = None

@app.on_event("startup")
def load_data():
    global data_df
    try:
        print("[INFO] Loading data from:", DATA_PATH)
        data_df = DataLoader(DATA_PATH).load_data()
        data_df = DataCleaner(data_df).clean()
        print("[INFO] Data loaded successfully.")
    except Exception as e:
        print("[ERROR] Failed to load data:", str(e))


# Pydantic model for POST
class ChatInput(BaseModel):
    conversation_id: str


@app.get("/")
def root():
    return {"message": "Welcome to the BiztelAI Chat Analysis API"}


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
        raise HTTPException(status_code=404, detail="Transcript ID not found")
    return Analyzer(data_df).summarize_chat(chat_df)


@app.get("/transform")
def transform_text(text: str):
    return {"transformed_text": TextProcessor().process_text(text)}
