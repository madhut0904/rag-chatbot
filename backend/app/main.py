from fastapi import FastAPI

app = FastAPI(
    title="Study RAG API",
    description="PDF Notes RAG API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Study RAG API is running"
    }


@app.get("/api/health")
def health():
    return {
        "status": "ok"
    }