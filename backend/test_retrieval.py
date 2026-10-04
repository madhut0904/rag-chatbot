from app.services.retrieval_service import retrieve_chunks


def main():

    question = "What is normalization in DBMS?"

    print("=" * 60)
    print("QUESTION")
    print(question)
    print("=" * 60)

    results = retrieve_chunks(
        question,
        limit=5
    )

    print(f"\nRetrieved results: {len(results)}")

    for index, result in enumerate(results, start=1):

        print("\n" + "=" * 60)
        print("RESULT:", index)
        print("Score:", result.score)

        payload = result.payload or {}

        print("File:", payload.get("filename"))
        print("Page:", payload.get("page_number"))
        print("Chunk:", payload.get("chunk_index"))

        print("\nTEXT:")
        print(payload.get("text"))


if __name__ == "__main__":
    main()