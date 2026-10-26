import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter } from 'react-router';
import './index.css';
import App from './App.jsx';

createRoot(document.getElementById('root')).render(
  //Step5:To use router we need to follow few steps. Need to surround App component with BrowserRouter like below
  <StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </StrictMode>,
)
