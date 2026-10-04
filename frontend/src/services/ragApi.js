const API_URL =
  import.meta.env.VITE_API_URL ||
  "http://127.0.0.1:8000";

export async function askRagQuestion({
  question,
  subjectId = null,
  documentIds = []
}) {
  const response = await fetch(
    `${API_URL}/api/chat`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        question,
        subject_id: subjectId,
        document_ids: documentIds
      })
    }
  );

  if (!response.ok) {
    const errorData =
      await response.json().catch(() => null);

    throw new Error(
      errorData?.detail ||
      "Failed to get answer from RAG backend"
    );
  }

  return response.json();
}