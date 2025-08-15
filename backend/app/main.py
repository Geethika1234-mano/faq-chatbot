from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


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
    Return an answer to the user's question.

    This endpoint currently returns a placeholder response. In a full
    implementation, you would load a company's FAQ and knowledge base, embed
    documents using a vector store, perform retrieval on the question, and
    generate an answer via a language model.
    """
    question = query.question
    # Placeholder logic. Replace with call to your retrieval + LLM pipeline.
    answer = f"This is a placeholder answer to the question: {question}"
    return {"question": question, "answer": answer}
