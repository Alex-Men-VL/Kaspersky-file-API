import { Descriptions } from 'antd'
import { OperatorDict } from 'modules/search/constants'

const SearchParams = ({ params }) => {
  const { text, fileMask, size, sizeOperator, creationDate, creationDateOperator } = params || {};

  return (
      <Descriptions column={1} size='small'>
        {text && (
            <Descriptions.Item label='Текст'>
              {text}
            </Descriptions.Item>
        )}
        {fileMask && (
            <Descriptions.Item label='Маска файла'>
              {fileMask}
            </Descriptions.Item>
        )}
        {size && sizeOperator && (
            <Descriptions.Item label='Размер'>
              {OperatorDict[sizeOperator]} {size}
            </Descriptions.Item>
        )}
        {creationDate && creationDateOperator && (
            <Descriptions.Item label='Дата создания'>
              {OperatorDict[creationDateOperator]} {new Date(creationDate).toLocaleString()}
            </Descriptions.Item>
        )}
      </Descriptions>
  )
}

export default SearchParams
