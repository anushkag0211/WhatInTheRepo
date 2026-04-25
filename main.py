from git import Repo

from loader import load_files
from chunker import chunk_text
from embedder import embedding_model
from retriever import retrieve
from rag import ask_rag

import faiss
import numpy as np

# ----------------------------
# Clone repo
# ----------------------------
repo_url = "https://github.com/psf/requests"
repo_path = "./repo"

Repo.clone_from(repo_url, repo_path)
print("Repo downloaded!")

# ----------------------------
# Load files
# ----------------------------
docs = load_files(repo_path)
print("Files loaded:", len(docs))

# ----------------------------
# Chunking
# ----------------------------
chunks = []

for doc in docs:
    for chunk in chunk_text(doc["text"]):
        chunks.append({
            "file": doc["file"],
            "text": chunk
        })

print("Total chunks:", len(chunks))

# ----------------------------
# Embeddings
# ----------------------------
texts = [c["text"] for c in chunks]
embeddings = embedding_model.encode(texts)

# ----------------------------
# FAISS index
# ----------------------------
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

# ----------------------------
# Final query function
# ----------------------------
def ask_codebase(query):
    retrieved = retrieve(query, embedding_model, index, chunks)
    answer = ask_rag(query, retrieved)

    return {
        "question": query,
        "answer": answer,
        "sources": list(set([r["file"] for r in retrieved]))
    }

# ----------------------------
# Run test
# ----------------------------
if __name__ == "__main__":
    result = ask_codebase("How does error handling work in this repo?")

    print("\nANSWER:\n", result["answer"])
    print("\nSOURCES:\n", result["sources"])
