from pydantic import BaseModel


class ChatRequest(BaseModel):
    question: str
    subject_id: str | None = None
    document_ids: list[str] = []


class Source(BaseModel):
    document_id: str
    filename: str
    page_number: int


class ChatResponse(BaseModel):
    answer: str
    sources: list[Source] = []