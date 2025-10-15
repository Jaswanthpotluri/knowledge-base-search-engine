from fastapi import FastAPI, Form
from src1.retriever import retrieve
from src1.llm_response import synthesize_answer
import yaml

app = FastAPI(title="Gemini Knowledge Base Search Engine")

with open("config/config.yaml") as f:
    config = yaml.safe_load(f)

@app.post("/query")
async def query_knowledgebase(query: str = Form(...)):
    context = retrieve(query, config["paths"]["vector_store"], config["embedding"]["model"])
    answer = synthesize_answer(query, context, config["llm"]["model_name"])
    return {"query": query, "answer": answer}
