import os
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from google import genai

app = FastAPI()
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

class Message(BaseModel):
    role: str          # "user" or "model"
    text: str

class ChatRequest(BaseModel):
    messages: list[Message]

@app.post("/chat")
def chat(req: ChatRequest):
    contents = [
        {"role": m.role, "parts": [{"text": m.text}]}
        for m in req.messages
    ]
    response = client.models.generate_content(
        model="gemini-flash-lite-latest",
        contents=contents,
    )
    return {"reply": response.text}

@app.get("/")
def home():
    return FileResponse("index.html")
