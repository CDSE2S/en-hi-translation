from fastapi import FastAPI, HTTPException
from models.translation_model import get_translator
# from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
translator = get_translator()

@app.get("/translate/")
def translate(text: str):
    result = translator(text)
    return {"translated_text": result[0]['translation_text']}


#error messages handling
@app.get("/translate/")
def translate(text: str):
    if not text.strip():
        raise HTTPException(status_code=400, detail="Input text cannot be empty.")
    result = translator(text)
    return {"translated_text": result[0]['translation_text']}


# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

