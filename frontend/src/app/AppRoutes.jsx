import { createBrowserRouter, RouterProvider } from 'react-router-dom'

import { routes } from 'configs/routes'

const AppRoutes = () => {
  const router = createBrowserRouter(routes)
  return <RouterProvider router={router} />
}

export default AppRoutes
