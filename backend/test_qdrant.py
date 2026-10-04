from app.services.vector_service import test_connection


if __name__ == "__main__":
    result = test_connection()

    print("Qdrant connection successful!")
    print(result)