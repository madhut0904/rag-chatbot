from app.services.embedding_service import create_embedding
from app.services.vector_service import client
from app.core.config import QDRANT_COLLECTION


def retrieve_chunks(
    question: str,
    limit: int = 5
):
    query_vector = create_embedding(question)

    response = client.query_points(
        collection_name=QDRANT_COLLECTION,
        query=query_vector,
        limit=limit,
        with_payload=True
    )

    return response.points