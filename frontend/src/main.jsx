import React from 'react'
import { createRoot } from 'react-dom/client'

import App from 'app/App'
import AppProvider from 'app/AppProvider';


const renderApp = () => {
  const rootElementId = 'root'
  const rootElement = document.getElementById(rootElementId)

  if (!rootElement) throw new Error(`Element by id - "${rootElementId}" was not found`)

  const root = createRoot(rootElement)

  root.render(
      <React.StrictMode>
        <AppProvider>
          <App />
        </AppProvider>
      </React.StrictMode>
  )
}

renderApp()
