import isPlainObject from 'lodash/isPlainObject'


import { HttpCodeEnum, HttpMethodEnum } from 'shared/constants/http'

import { makeRelativeApiUrl } from 'shared/services/baseApi/utils'
import httpClient from './httpClient'
import {MimetypeEnum} from 'shared/constants/mimetype';

const baseQuery =
  ({ basePath, apiVersion }) =>
  async ({ url, method = HttpMethodEnum.Get, data, params, headers }) => {
    try {
      const response = await httpClient({
        url: makeRelativeApiUrl(url, basePath, apiVersion),
        method,
        data,
        params,
        headers: {
          'Content-Type': MimetypeEnum.Json,
          ...headers,
        }
      })

      return { data: response.data, meta: { response } }
    } catch (exception) {
      const error = exception
      const status = error.response?.status || HttpCodeEnum.ServerError
      const errorData = error.response?.data

      return {
        error: {
          status,
          data: isPlainObject(errorData)
            ? errorData
            : { detail: ['Неизвестная ошибка'] }
        }
      }
    }
  }

export default baseQuery
