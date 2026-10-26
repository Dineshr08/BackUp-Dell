import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'

//Step4:Here main.js is setup react code, gain removed ReactDOM same concept as Step3.Here we have used StrictMode component as it will check for more rules and warning .
createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
