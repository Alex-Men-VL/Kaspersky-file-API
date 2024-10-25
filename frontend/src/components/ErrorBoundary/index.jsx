import {isRouteErrorResponse, Link, useRouteError} from 'react-router-dom'
import {isNotFoundError} from 'shared/services/baseApi'
import {Flex, Typography} from 'antd';
import {CommonRouteEnum} from 'configs/routes';

const { Title } = Typography

const renderError = (message) => {
  return (
      <Flex vertical align='center' gap='middle'>
        <Title level={5}>{message}</Title>
        <Link to={CommonRouteEnum.Root}>Перейти на главную</Link>
      </Flex>
  )
}

const ErrorBoundary = () => {
  const error = useRouteError()

  if (isRouteErrorResponse(error)) {
    if (isNotFoundError(error)) {
      return renderError('Страница не найдена')
    }
  }

  return renderError('Ошибка. Что-то пошло не так')
}

export default ErrorBoundary