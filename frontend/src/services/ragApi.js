const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

export const askRagQuestion = async (query, conversationId = null) => {
  const response = await fetch(`${API_BASE_URL}/api/chat`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ query, conversation_id: conversationId }),
  });

  if (!response.ok) {
    throw new Error(`RAG API Error: ${response.statusText}`);
  }

  return response.json();
};

export default {
  askRagQuestion,
};
