import { useState, useCallback } from 'react';
import { askRagQuestion } from '../services/ragApi';

export const useChat = () => {
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const sendMessage = useCallback(async (text) => {
    if (!text.trim()) return;

    const userMessage = { sender: 'user', text };
    setMessages((prev) => [...prev, userMessage]);
    setLoading(true);
    setError(null);

    try {
      const data = await askRagQuestion(text);
      const botMessage = {
        sender: 'assistant',
        text: data?.answer || data?.response || 'No response received.',
        sources: data?.sources || [],
      };
      setMessages((prev) => [...prev, botMessage]);
    } catch (err) {
      setError(err.message || 'Failed to fetch response');
      setMessages((prev) => [
        ...prev,
        { sender: 'assistant', text: 'Sorry, something went wrong. Please try again.', error: true },
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
    setMessages,
  };
};

export default useChat;
