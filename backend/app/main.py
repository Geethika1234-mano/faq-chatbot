from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import openai

app = FastAPI(title="FAQ Chatbot")

# Configure CORS to allow local frontend access during development. In production,
# you should restrict allowed origins to your deployment domains.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Read OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

class Query(BaseModel):
    """Schema for incoming chat questions."""
    question: str

@app.get("/")
async def read_root() -> dict[str, str]:
    """Health check endpoint to verify the API is running."""
    return {"message": "FAQ Chatbot API is running"}

@app.post("/chat")
async def chat(query: Query) -> dict[str, str]:
    """
    Return an answer to the user's question using OpenAI's chat model.
    """
    messages = [
        {"role": "system", "content": "You are a helpful FAQ chatbot."},
        {"role": "user", "content": query.question},
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=200,
        temperature=0.3,
    )
    answer = response.choices[0].message.content.strip()
    return {"question": query.question, "answer": answer}
