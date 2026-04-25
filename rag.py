from llm import generate_answer

def build_prompt(query, retrieved_chunks):

    context = ""

    for c in retrieved_chunks:
        context += f"\nFile: {c['file']}\nCode:\n{c['text']}\n---\n"

    return f"""
You are a senior software engineer.

Answer clearly in 5–7 lines.

Do NOT repeat code.
Do NOT stop mid-sentence.

If unsure, say "Not enough information."

QUESTION:
{query}

CODE:
{context}

ANSWER:
"""


def ask_rag(query, retrieved_chunks):
    prompt = build_prompt(query, retrieved_chunks)
    return generate_answer(prompt)
