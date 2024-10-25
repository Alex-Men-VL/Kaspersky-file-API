import { SyncOutlined } from '@ant-design/icons'
import { Button, Row, Typography } from 'antd'
import { getSearchIdTitle } from 'modules/search/utils'

const { Text } = Typography

const SearchDetailTitle = ({searchId, onReload}) => {
  return (
      <Row justify='space-between' align='middle'>
        <Text>{getSearchIdTitle(searchId)}</Text>

        <Button type='text' icon={<SyncOutlined />} onClick={onReload} />
      </Row>
  )
}

export default SearchDetailTitle