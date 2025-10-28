from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline, Conversation
import uvicorn

# Load conversational pipeline (make sure to pip install fastapi uvicorn transformers torch pydantic)
chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")

app = FastAPI()

class ChatRequest(BaseModel):
    user_input: str

@app.post("/chat")
async def chat_endpoint(chat: ChatRequest):
    conversation = Conversation(chat.user_input)
    response = chatbot([conversation])
    answer = response[0].generated_responses[-1]
    return {"response": answer}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
