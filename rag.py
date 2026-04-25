from llm import generate_answer

def build_prompt(query, retrieved_chunks):

    context = ""

    for c in retrieved_chunks[:2]:
        context += f"\nFile: {c['file']}\n{c['text']}\n"

    return f"""
You are a senior software engineer analyzing code.

Answer the question clearly in 3-5 sentences.

Only use the provided code.
Do not generate extra questions or sections.
If the answer is not in the code, say: "Not enough information."

Question: {query}

Code:
{context}

Answer:
"""


def ask_rag(query, retrieved_chunks):
    prompt = build_prompt(query, retrieved_chunks)
    return generate_answer(prompt)
