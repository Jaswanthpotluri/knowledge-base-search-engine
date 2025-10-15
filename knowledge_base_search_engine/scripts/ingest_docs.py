import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # ✅ adds project root to Python path

from src1.data_ingestion import ingest_documents

from src1.embedding_store import create_embeddings
import yaml

with open("D:\ml\knowledge_base_search_engine\config\config.yaml") as f:
    config = yaml.safe_load(f)

ingest_documents(config["paths"]["raw_data"], config["paths"]["processed_data"])
create_embeddings(
    config["paths"]["processed_data"],
    config["paths"]["vector_store"],
    
)
