import { env } from 'configs/env'

import { MimetypeEnum } from 'shared/constants/mimetype'

import { toJsonTransformer, toSnakeCaseTransformer } from './requestTransformers'
import { fromJsonTransformer, fromSnakeCaseTransformer } from './responseTransformers'

const config = {
  baseURL: env.get('apiUrl'),
  headers: {
    'Content-Type': MimetypeEnum.Json
  },
  transformRequest: [toSnakeCaseTransformer, toJsonTransformer],
  transformResponse: [fromJsonTransformer, fromSnakeCaseTransformer],
}

export default config
