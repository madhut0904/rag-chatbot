import { useState } from "react";
import ChatWindow from "../../components/rag/ChatWindow";

export default function StudyAssistant() {
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSend = async (question) => {
    setMessages((prev) => [
      ...prev,
      {
        role: "user",
        content: question
      }
    ]);

    setLoading(true);

    // Temporary placeholder.
    // Real backend connection comes later.
    setTimeout(() => {
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: "The RAG backend is not connected yet."
        }
      ]);

      setLoading(false);
    }, 500);
  };

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <ChatWindow
        messages={messages}
        onSend={handleSend}
        loading={loading}
      />
    </div>
  );
}