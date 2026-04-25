# WhatInTheRepo
GenAI-powered RAG system that explains any GitHub repository by retrieving relevant code using FAISS and generating clear, high-quality explanations using LLMs (Phi-3 + SentenceTransformers).

Link to google collab- https://colab.research.google.com/github/anushkag0211/WhatInTheRepo/blob/main/WhatInRepo1.ipynb

## What it does
- Clones any GitHub repository
- Splits code into meaningful chunks
- Generates embeddings using Sentence Transformers
- Retrieves relevant code using FAISS similarity search
- Uses Phi-3 LLM to generate explanations

---

## Tech Stack
- Python
- FAISS
- SentenceTransformers
- HuggingFace Transformers
- Phi-3 Mini LLM
- GitPython

---

## Architecture
1. Load repository files
2. Chunk code into segments
3. Convert chunks into embeddings
4. Store embeddings in FAISS index
5. Retrieve top-k relevant chunks
6. Send to LLM for explanation

---

## Example
**Question:** How does error handling work in this repo?

**Output:** Clear explanation based only on retrieved code context.

---

## Run
```bash
pip install -r requirements.txt
python main.py
