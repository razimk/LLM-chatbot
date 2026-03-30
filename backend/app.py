from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

# ✅ ADD CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Answer shortly."),
    ("user", "Question: {question}")
])

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama-3.1-8b-instant"
)

parser = StrOutputParser()
chain = prompt | llm | parser


class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
def chat(request: ChatRequest):
    response = chain.invoke({"question": request.message})
    return {"response": response}


@app.get("/")
def home():
    return {"message": "Chatbot API is running"}