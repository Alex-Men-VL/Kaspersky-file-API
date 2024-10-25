import get from 'lodash/get'

const getContentType = (headers) => {
  return get(headers, 'Content-Type', '') || get(headers, 'content-type', '')
}

export default getContentType
