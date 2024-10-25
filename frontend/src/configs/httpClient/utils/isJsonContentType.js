import { MimetypeEnum } from 'shared/constants/mimetype'

const isJsonContentType = (type) => {
  return type.includes(MimetypeEnum.Json)
}

export default isJsonContentType
