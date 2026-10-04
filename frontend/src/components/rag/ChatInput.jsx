import { useState } from "react";

export default function ChatInput({ onSend, disabled }) {
  const [question, setQuestion] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!question.trim() || disabled) return;

    onSend(question.trim());
    setQuestion("");
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="flex gap-2 border-t p-4"
    >
      <input
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask something from your notes..."
        className="flex-1 rounded-xl border px-4 py-3 outline-none"
        disabled={disabled}
      />

      <button
        type="submit"
        disabled={disabled}
        className="rounded-xl bg-blue-600 px-5 py-3 text-white disabled:opacity-50"
      >
        Ask
      </button>
    </form>
  );
}