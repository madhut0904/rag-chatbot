export default function SourceCard({ source }) {
  if (!source) return null;

  return (
    <div className="mt-2 inline-flex items-center gap-2 rounded-lg border border-gray-200 bg-white px-3 py-1.5 text-xs text-gray-700 shadow-sm">
      <span className="font-medium text-gray-900">{source.filename}</span>
      {source.page_number && (
        <span className="rounded bg-blue-50 px-1.5 py-0.5 font-semibold text-blue-700">
          Page {source.page_number}
        </span>
      )}
    </div>
  );
}
