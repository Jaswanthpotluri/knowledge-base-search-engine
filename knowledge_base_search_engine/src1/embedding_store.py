from sentence_transformers import SentenceTransformer
import os
import pickle

def create_embeddings(processed_dir, model_path):
    """
    Generate and save embeddings for all processed text documents.
    """
    model = SentenceTransformer("all-MiniLM-L6-v2")

    embeddings = []
    texts = []

    for file in os.listdir(processed_dir):
        if file.endswith(".txt"):
            file_path = os.path.join(processed_dir, file)
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()
                texts.append(text)
                emb = model.encode(text)
                embeddings.append(emb)

    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    with open(model_path, "wb") as f:
        pickle.dump({"embeddings": embeddings, "texts": texts}, f)

    print("✅ Embeddings created and stored successfully.")
