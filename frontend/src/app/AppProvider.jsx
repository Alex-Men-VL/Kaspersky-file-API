import { App } from 'antd'
import React from 'react'
import { Provider as StoreProvider } from 'react-redux'

import { store as appStore } from '../state/store'

const AppProvider = ({ children, store=appStore }) => {
  return (
    <App>
      <StoreProvider store={store}>{children}</StoreProvider>
    </App>
  )
}

export default AppProvider
