import { notification } from 'antd'

export const showSuccessNotification = (message, options = {}) => {
  notification.success({
    message: message,
    ...options
  })
}
