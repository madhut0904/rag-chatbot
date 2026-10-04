from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

from app.core.config import (
    QDRANT_URL,
    QDRANT_API_KEY,
    QDRANT_COLLECTION
)


client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY
)


def ensure_collection_exists(vector_size: int = 3072):
    if not client.collection_exists(collection_name=QDRANT_COLLECTION):
        client.create_collection(
            collection_name=QDRANT_COLLECTION,
            vectors_config=VectorParams(
                size=vector_size,
                distance=Distance.COSINE
            )
        )