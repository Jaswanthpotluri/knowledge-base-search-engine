from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import yaml, os
from src1.retriever import retrieve
from src1.llm_response import generate_answer
import google.generativeai as genai
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


app = FastAPI(title="Knowledge Base Search Engine")

# Load configuration
with open("config/config.yaml") as f:
    config = yaml.safe_load(f)

# Configure Gemini API key
os.environ["GOOGLE_API_KEY"] = "YOUR_API_KEY"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Serve frontend static files
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

@app.get("/")
async def root():
    return FileResponse("frontend/index.html")

@app.post("/query")
async def query_knowledgebase(query: str = Form(...)):
    context = retrieve(
        query=query,
        vector_store_path=config["paths"]["vector_store"],
        model_name=config["embedding"]["model"]
    )
    answer = generate_answer(
        question=query,
        context=context,
        model_name=config["llm"]["model_name"],
        temperature=config["llm"]["temperature"]
    )
    return {"query": query, "answer": answer}
