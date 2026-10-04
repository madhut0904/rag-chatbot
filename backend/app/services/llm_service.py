from google import genai

from app.core.config import GEMINI_API_KEY


client = genai.Client(
    api_key=GEMINI_API_KEY
)


GEMINI_MODEL = "gemini-3.8-flash"


SYSTEM_INSTRUCTION = """
You are a study assistant for students.

Answer questions ONLY using the context provided to you.

STRICT RULES:

1. Use only the supplied context.
2. Do not use outside knowledge.
3. Do not invent facts.
4. Do not invent examples.
5. Do not invent PDF names.
6. Do not invent page numbers.
7. If the answer cannot be found in the supplied context,
   respond exactly:

"I couldn't find this information in the uploaded notes."

8. If the context contains only part of the answer,
   clearly explain only what is supported by the context.
9. Make answers clear and suitable for a college student.
10. Use headings, bullet points, and numbered lists when useful.
"""


def generate_answer(question: str, context: str):

    prompt = f"""
{SYSTEM_INSTRUCTION}

QUESTION:
{question}

CONTEXT FROM UPLOADED NOTES:
{context}

Answer the question using ONLY the supplied context.
"""

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt
    )

    return response.text