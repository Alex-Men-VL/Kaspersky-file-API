import inRange from 'lodash/inRange'
import isEqual from 'lodash/isEqual'
import isNumber from 'lodash/isNumber'
import isObject from 'lodash/isObject'

import { HttpCodeEnum } from 'shared/constants'
import { hasProperty } from 'shared/utils/common'
import {apiPath, currentApiVersion} from 'shared/services/baseApi/constants';
import {makeString} from 'shared/utils/string';
import isString from 'lodash/isString';

export const getErrorMessage = (error) => {
  return error.data?.message || ''
}

export const getRelativeApiUrl = (basePath = apiPath, apiVersion = currentApiVersion) => makeString('/', basePath, apiVersion)

export const makeRelativeApiUrl = (path, basePath = apiPath, apiVersion = currentApiVersion) =>
    makeString('', getRelativeApiUrl(basePath, apiVersion), path)

export const isErrorResponse = (response) => {
  if (!isObject(response)) {
    return false
  }

  return !!(hasProperty(response, 'status') && isNumber(response.status) && hasProperty(response, 'data') && isObject(response.data))
}

export const isServerRangeError = (error) => inRange(error.status, HttpCodeEnum.ServerError, HttpCodeEnum.InvalidSSLCertificate)

export const isNotFoundError = (error) => isEqual(error.status, HttpCodeEnum.NotFound)

export const isBadRequestError = (error) => isEqual(error.status, HttpCodeEnum.BadRequest)
