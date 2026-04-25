from transformers import pipeline

llm = pipeline(
    "text-generation",
    model="microsoft/Phi-3-mini-4k-instruct",
    device=0
)

def generate_answer(prompt):
    output = llm(
        prompt,
        max_new_tokens=300,
        temperature=0.2,
        return_full_text=False
    )

    return output[0]["generated_text"].strip()
