from app.services.embedding_service import create_embedding


def main():
    text = "Normalization is a database design technique used to reduce redundancy."

    print("Creating embedding...")

    vector = create_embedding(text)

    print("Embedding created successfully.")
    print("Vector dimension:", len(vector))
    print("First 5 values:", vector[:5])


if __name__ == "__main__":
    main()