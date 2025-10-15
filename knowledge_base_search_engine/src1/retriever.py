import numpy as np
import pickle
from sentence_transformers import SentenceTransformer

def retrieve(query, vector_store_path, model_name, top_k=3):
    """Retrieve top-K relevant documents based on similarity."""
    model = SentenceTransformer(model_name)
    with open(vector_store_path, "rb") as f:
        store = pickle.load(f)

    query_emb = model.encode([query])[0]
    sims = np.dot(store["embeddings"], query_emb)
    top_k_idx = np.argsort(sims)[-top_k:][::-1]
    return [store["texts"][i] for i in top_k_idx]
