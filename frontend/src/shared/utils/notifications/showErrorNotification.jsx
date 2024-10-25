import { notification } from 'antd'

export const showErrorNotification = (errorOrErrorList, options = {}) => {
  if (Array.isArray(errorOrErrorList)) {
    if (errorOrErrorList.length) {
      errorOrErrorList.forEach((error) => {
        notification.error({ message: error, ...options })
      })
    }
  } else {
    notification.error({ message: errorOrErrorList, ...options })
  }
}
