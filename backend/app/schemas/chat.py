from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    question: str
    subject_id: str | None = None
    document_ids: list[str] = Field(default_factory=list)


class Source(BaseModel):
    document_id: str
    filename: str
    page_number: int | None = None


class ChatResponse(BaseModel):
    answer: str
    sources: list[Source] = Field(default_factory=list)