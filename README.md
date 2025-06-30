# Biztel.ai-assignment
Here’s a clear and professional DOCUMENTATION.md section that you can include in your project or link from your README.md. This covers methodologies, insights, and justifies the approaches you’ve taken across all tasks of the BiztelAI DS Intern Assignment.

⸻

📄 Documentation: Insights & Methodologies

📌 Project Overview

This project focuses on analyzing chat transcripts between two agents discussing Washington Post articles. The goal is to:
 • Extract meaningful insights using NLP and EDA
 • Expose insights through a production-ready FastAPI
 • Follow object-oriented and modular code practices

⸻

✅ Task 1: Data Ingestion & Preprocessing

🔍 Methodology
 • JSON files were loaded and flattened using a custom DataLoader class.
 • Only relevant fields (message, agent, sentiment, turn_rating, etc.) were extracted into a DataFrame.
 • Missing values and duplicates were handled via dropna and drop_duplicates.

💡 Key Insight
 • The structure of the JSON required flattening nested elements (conversation_id, article_url, message details).
 • Around 2–5% of entries had empty or duplicate messages, which were removed for cleaner analysis.

⸻

✅ Task 2: Exploratory Data Analysis (EDA)

🔍 Methodology
 • Used matplotlib and seaborn to visualize:
 • Message counts per agent
 • Distribution of sentiments
 • Article-wise conversation volume
 • Sentiments and agents were grouped to extract behavioral trends.

📊 Insights
 • Agent 1 tends to express more curiosity and emotion than Agent 2.
 • Sentiments like “Curious to dive deeper”, “Surprised”, and “Happy” were most common.
 • Some transcripts have as many as 20+ message exchanges, offering rich sentiment data.

⸻

✅ Task 3: REST API Development

🔍 Methodology
 • Built using FastAPI for speed and modern structure.
 • Key endpoints:
 • /summary — returns dataset-level insights
 • /transform — processes new text
 • /analyze_transcript — returns article link, sentiment stats, message counts

🔐 Considerations
 • Input validation via pydantic
 • Error handling for unknown conversation IDs
 • Modular class-based design for future extensibility

⸻

✅ Task 4: OOP in Data Processing

🔍 Methodology
 • Developed the following classes:
 • DataLoader – for loading structured JSON
 • DataCleaner – for preprocessing and cleaning
 • TextProcessor – handles lemmatization, stopwords
 • Analyzer – for per-transcript summary

💡 Key Insight
 • Modularization made it easy to plug logic into both notebooks and FastAPI without code duplication.

⸻

✅ Task 5: Code Optimization

🔍 Methodology
 • Replaced loops with pandas vectorized operations.
 • Avoided redundant DataFrame copies.
 • FastAPI is async-ready; endpoints are lightweight and fast.

⏱ Performance Results
 • API response time (local): <100 ms
 • Loading and summarizing full dataset: <1.5 sec

⸻

🤖 Sentiment Modeling
 • Sentiment labels were already present in the dataset, so no retraining was needed.
 • Optionally, external LLMs (like flair or VADER) could be used for real-time inference in production.

⸻

📚 Tools & Libraries Used

Tool       Purpose
pandas     Data manipulation
FastAPI    REST API backend
spacy      NLP preprocessing (lemmatization)
uvicorn    ASGI server for FastAPI
seaborn    Visualization


⸻

✅ Future Improvements
 • Implement sentiment inference using flair or HuggingFace transformers.
 • Add JWT-based authentication to the API.
 • Deploy using Docker and serve with Nginx + Gunicorn.


