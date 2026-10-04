import ChatMessage from "./ChatMessage";
import ChatInput from "./ChatInput";

export default function ChatWindow({
  messages,
  onSend,
  loading
}) {
  return (
    <div className="mx-auto flex h-[700px] max-w-4xl flex-col overflow-hidden rounded-2xl border bg-white shadow">

      <div className="border-b p-5">
        <h1 className="text-xl font-semibold">
          Study Assistant
        </h1>

        <p className="text-sm text-gray-500">
          Ask questions from your uploaded notes
        </p>
      </div>

      <div className="flex-1 overflow-y-auto p-5">
        {messages.length === 0 && (
          <div className="flex h-full items-center justify-center text-gray-500">
            Ask a question about your notes.
          </div>
        )}

        {messages.map((message, index) => (
          <ChatMessage
            key={index}
            role={message.role}
            content={message.content}
          />
        ))}

        {loading && (
          <div className="text-sm text-gray-500">
            Searching your notes...
          </div>
        )}
      </div>

      <ChatInput
        onSend={onSend}
        disabled={loading}
      />
    </div>
  );
}