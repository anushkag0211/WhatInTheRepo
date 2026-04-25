import numpy as np

def retrieve(query, embedding_model, index, chunks, k=2):
    query_embedding = embedding_model.encode([query])
    distances, indices = index.search(np.array(query_embedding), k)

    return [chunks[i] for i in indices[0]]
