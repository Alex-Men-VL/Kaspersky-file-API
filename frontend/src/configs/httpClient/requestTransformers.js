import { decamelizeKeys } from 'humps'

import { hasJsonContentType } from 'configs/httpClient/utils'

const toJsonTransformer = (data, headers) => {
  return hasJsonContentType(headers) ? JSON.stringify(data) : data
}

const toSnakeCaseTransformer = (data, headers) => {
  return hasJsonContentType(headers) && data ? decamelizeKeys(data) : data
}

export { toJsonTransformer, toSnakeCaseTransformer }
