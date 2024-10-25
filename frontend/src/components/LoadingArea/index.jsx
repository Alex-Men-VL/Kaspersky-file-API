import React from 'react'
import Spinner from 'components/Spinner'

const LoadingArea = ({ children, isLoading, ...props }) => {
  return isLoading ? <Spinner {...props} /> : <>{children}</>
}

export default LoadingArea
