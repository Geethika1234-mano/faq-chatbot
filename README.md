# faq-chatbot

A custom FAQ chatbot for company websites. This project provides an API and a simple web interface to answer customer questions using an AI language model and retrieval of a company's FAQ documents.

## Overview

This chatbot helps visitors get quick answers by matching their queries with your website's FAQ and knowledge base. It uses natural language processing and embeddings to understand the user's question, retrieves the most relevant FAQ entries and generates a helpful answer.

## Features

- **FastAPI backend:** A modern, async web API built with FastAPI and Uvicorn, configured with CORS support for local development.
- **Chat endpoint:** A `/chat` endpoint that accepts a question and returns an answer. The current implementation returns a placeholder answer to illustrate the API contract.
- **Simple frontend:** A lightweight HTML/CSS/JavaScript interface for chatting with the bot.
- **Extensible architecture:** The placeholder logic is ready to be replaced with retrieval-augmented generation using LangChain and the OpenAI API or another LLM provider.
- **Easy deployment:** Run locally with `uvicorn` and serve the frontend with `python -m http.server`, or containerize for deployment.

## Tech Stack

- **Backend:** Python, FastAPI, Uvicorn, Pydantic
- **AI/Retrieval:** LangChain, OpenAI (to be integrated)
- **Frontend:** HTML, CSS, JavaScript

## Running Locally

1. **Clone the repository** (if you haven't already):

   ```bash
   git clone https://github.com/Geethika1234-mano/faq-chatbot.git
   cd faq-chatbot
   ```

2. **Install dependencies** (preferably inside a virtual environment):

   ```bash
   pip install -r backend/requirements.txt
   ```

3. **Start the backend API server:**

   ```bash
   uvicorn backend.app.main:app --reload
   ```

   The API will be available at `http://127.0.0.1:8000`.

4. **Serve the frontend:**

   In a new terminal, run:

   ```bash
   cd frontend
   python3 -m http.server 5500
   ```

   Then open `http://localhost:5500` in your browser. You can ask questions in the chat interface.

5. **Extend the chatbot:**

   The current implementation returns placeholder answers. To integrate a real AI model, modify the `chat()` function in `backend/app/main.py` to perform retrieval from your FAQ documents and generate a response using a language model. You can use LangChain's retrieval-augmented generation utilities with embeddings and the OpenAI API.

## Contributing

Pull requests are welcome! Feel free to open an issue or discussion to propose changes, enhancements or ask questions.
