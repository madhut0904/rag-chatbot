from app.services.rag_service import answer_question


def main():

    question = "What is quantum teleportation?"

    print("=" * 60)
    print("QUESTION")
    print(question)
    print("=" * 60)

    result = answer_question(question)

    print("\nANSWER")
    print("=" * 60)
    print(result["answer"])

    print("\nSOURCES")
    print("=" * 60)

    for source in result["sources"]:

        print(
            f"- {source['filename']} "
            f"(Page {source['page_number']})"
        )


if __name__ == "__main__":
    main()