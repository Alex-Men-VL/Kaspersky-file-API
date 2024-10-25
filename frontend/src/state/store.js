import { configureStore } from '@reduxjs/toolkit'

import { baseApiService } from 'shared/services/baseApi'


export const setupStore = () => {
  return configureStore({
    reducer: {
      [baseApiService.reducerPath]: baseApiService.reducer,
    },
    middleware: (getDefaultMiddleware) =>
      getDefaultMiddleware().concat(baseApiService.middleware),
  })
}

export const store = setupStore()
