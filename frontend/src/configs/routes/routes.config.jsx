import React from 'react'

import ErrorBoundary from 'components/ErrorBoundary'
import HomeLayout from 'components/Layouts/HomeLayout'

import { CommonRouteEnum } from 'configs/routes/constants'

const SearchPage = React.lazy(() => import('modules/search/pages/SearchPage'))

export const routes = [
  {
    path: CommonRouteEnum.Root,
    errorElement: <ErrorBoundary />,
    element: <HomeLayout />,
    children: [
      {
        index: true,
        element: <SearchPage/>
      },
    ]
  }
]
