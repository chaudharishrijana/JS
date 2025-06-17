// src/main.jsx
import React from 'react';
import ReactDOM from 'react-dom/client'; // ✅ Correct import for React 18+
import App from './App.jsx';
import { StrictMode } from 'react'; // ✅ Make sure StrictMode is imported

const root = ReactDOM.createRoot(document.getElementById('root')); // ✅ Use createRoot
root.render(
  <StrictMode>
    <App />
  </StrictMode>
);
