import SourceCard from "./SourceCard";

export default function ChatMessage({ role, content, sources = [] }) {
  const isUser = role === "user";

  return (
    <div className={`flex ${isUser ? "justify-end" : "justify-start"} mb-4`}>
      <div
        className={`max-w-[85%] rounded-2xl px-4 py-3 ${
          isUser
            ? "bg-blue-600 text-white"
            : "border border-gray-200 bg-gray-50 text-gray-900"
        }`}
      >
        <div className="whitespace-pre-wrap leading-relaxed text-sm">{content}</div>

        {!isUser && sources && sources.length > 0 && (
          <div className="mt-3 border-t border-gray-200/60 pt-2">
            <p className="text-xs font-semibold uppercase tracking-wider text-gray-500">
              Sources
            </p>
            <div className="mt-1 flex flex-wrap gap-2">
              {sources.map((source, index) => (
                <SourceCard key={index} source={source} />
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
