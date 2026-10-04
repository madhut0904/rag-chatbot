from fastapi import APIRouter, HTTPException

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.rag_service import answer_question


router = APIRouter(
    prefix="/api/chat",
    tags=["Chat"]
)


@router.post("", response_model=ChatResponse)
async def chat(request: ChatRequest):

    question = request.question.strip()

    if not question:
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty"
        )

    result = answer_question(
        question=question
    )

    return ChatResponse(
        answer=result["answer"],
        sources=result["sources"]
    )