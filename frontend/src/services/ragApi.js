const API_URL =
  import.meta.env.VITE_API_URL || "http://localhost:8000";

export async function askQuestion(data) {
  const response = await fetch(`${API_URL}/api/chat`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
  });

  if (!response.ok) {
    throw new Error("Failed to contact RAG server");
  }

  return response.json();
}