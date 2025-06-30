#text_processor.py
import spacy

class TextProcessor:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def process_text(self, text: str) -> str:
        doc = self.nlp(text)
        tokens = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]
        return " ".join(tokens)