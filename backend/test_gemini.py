from google import genai
from app.core.config import GEMINI_API_KEY, GEMINI_MODEL

client = genai.Client(api_key=GEMINI_API_KEY)


def main():
    print("Testing Gemini...")
    print("Model:", GEMINI_MODEL)

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents="Say hello in one short sentence."
    )

    print("\nGemini response:")
    print(response.text)


if __name__ == "__main__":
    main()