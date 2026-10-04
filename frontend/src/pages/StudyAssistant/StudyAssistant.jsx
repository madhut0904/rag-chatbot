import { useEffect, useState } from "react";
import ChatWindow from "../../components/rag/ChatWindow";
import { useChat } from "../../hooks/useChat";

const API_URL =
  import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

export default function StudyAssistant() {
  const { messages, loading, sendMessage } = useChat();
  const [backendConnected, setBackendConnected] = useState(null);

  useEffect(() => {
    async function checkHealth() {
      try {
        const response = await fetch(`${API_URL}/api/health`);
        if (response.ok) {
          const data = await response.json();
          if (data?.status === "ok") {
            setBackendConnected(true);
            return;
          }
        }
        setBackendConnected(false);
      } catch {
        setBackendConnected(false);
      }
    }

    checkHealth();
  }, []);

  return (
    <div className="min-h-screen bg-gray-50 p-6 flex flex-col items-center">
      <div className="w-full max-w-4xl mb-3 flex items-center justify-between">
        <div className="text-sm font-medium">
          {backendConnected === true && (
            <span className="inline-flex items-center gap-1.5 text-emerald-600 bg-emerald-50 border border-emerald-200 px-3 py-1 rounded-full text-xs">
              <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
              RAG backend connected
            </span>
          )}
          {backendConnected === false && (
            <span className="inline-flex items-center gap-1.5 text-red-600 bg-red-50 border border-red-200 px-3 py-1 rounded-full text-xs">
              <span className="w-2 h-2 rounded-full bg-red-500"></span>
              RAG backend is not connected
            </span>
          )}
          {backendConnected === null && (
            <span className="inline-flex items-center gap-1.5 text-gray-500 bg-gray-100 border border-gray-200 px-3 py-1 rounded-full text-xs">
              Checking backend connection...
            </span>
          )}
        </div>
      </div>

      <ChatWindow
        messages={messages}
        onSend={sendMessage}
        loading={loading}
      />
    </div>
  );
}