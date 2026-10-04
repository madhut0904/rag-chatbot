import { useState, useCallback } from "react";
import { askRagQuestion } from "../services/ragApi";

export function useChat() {
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const sendMessage = useCallback(async (question) => {
    if (!question || !question.trim()) return;

    const trimmedQuestion = question.trim();

    setMessages((prev) => [
      ...prev,
      {
        role: "user",
        content: trimmedQuestion
      }
    ]);

    setLoading(true);
    setError(null);

    try {
      const result = await askRagQuestion({
        question: trimmedQuestion
      });

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: result.answer,
          sources: result.sources || []
        }
      ]);
    } catch (err) {
      const errorMessage =
        err?.message || "Failed to get answer from RAG backend";
      setError(errorMessage);

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: errorMessage,
          error: true,
          sources: []
        }
      ]);
    } finally {
      setLoading(false);
    }
  }, []);

  return {
    messages,
    loading,
    error,
    sendMessage,
    setMessages
  };
}

export default useChat;
