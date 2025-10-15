import sys
import os
import yaml
import google.generativeai as genai

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src1.retriever import retrieve
from src1.llm_response import generate_answer

# Load configuration file
with open(r"D:\ml\knowledge_base_search_engine\config\config.yaml") as f:
    config = yaml.safe_load(f)

# Configure Gemini API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyCh0jIBcaj4rZMK5PZrGX6atREDvEBdYPo"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Set the model explicitly (choose from the list you got)
TEXT_GEN_MODEL = "models/gemini-2.5-flash"  # ✅ Replace if needed

# Take user query
query = input("Enter your question: ")

# Retrieve relevant context
vector_store_path = os.path.abspath(config["paths"]["vector_store"])
context = retrieve(
    query=query,
    vector_store_path=vector_store_path,
    model_name=config["embedding"]["model"]
)

# Combine context and query into a single prompt
prompt = f"Context:\n{context}\n\nQuestion:\n{query}\n\nAnswer:"

# Generate final answer using Gemini
answer = generate_answer(
    prompt=prompt,
    temperature=config["llm"]["temperature"],
    model_name=TEXT_GEN_MODEL
)

# Print the answer
print("\n🧩 Answer:")
print(answer)
