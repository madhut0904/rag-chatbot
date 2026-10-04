from app.services.retrieval_service import retrieve_chunks
from app.services.llm_service import generate_answer


def answer_question(question: str):

    results = retrieve_chunks(
        question=question,
        limit=5
    )

    if not results:
        return {
            "answer": "I couldn't find this information in the uploaded notes.",
            "sources": []
        }

    context_parts = []
    sources = []

    for result in results:

        payload = result.payload or {}

        text = payload.get("text", "")
        filename = payload.get(
            "filename",
            "Unknown"
        )
        page_number = payload.get(
            "page_number"
        )

        context_parts.append(
            f"""
SOURCE:
File: {filename}
Page: {page_number}

CONTENT:
{text}
"""
        )

        sources.append({
            "document_id": payload.get(
                "document_id",
                ""
            ),
            "filename": filename,
            "page_number": page_number
        })

    context = "\n\n".join(context_parts)

    answer = generate_answer(
        question=question,
        context=context
    )

    return {
        "answer": answer,
        "sources": sources
    }