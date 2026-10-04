import React from 'react';

export const SourceCard = ({ source }) => {
  return (
    <div className="source-card">
      <h4>{source?.title || 'Source'}</h4>
      <p>{source?.content}</p>
    </div>
  );
};

export default SourceCard;
