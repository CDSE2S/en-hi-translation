from transformers import pipeline

def get_translator():
    return pipeline("translation_en_to_hi", model="Helsinki-NLP/opus-mt-en-hi")