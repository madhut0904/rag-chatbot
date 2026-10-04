from app.services.vector_service import client
from app.core.config import QDRANT_COLLECTION


def main():
    info = client.get_collection(
        collection_name=QDRANT_COLLECTION
    )

    print("Collection:", QDRANT_COLLECTION)
    print("Points:", info.points_count)
    print("Status:", info.status)


if __name__ == "__main__":
    main()