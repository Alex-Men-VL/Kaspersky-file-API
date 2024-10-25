import {Space} from 'antd'


const SearchStatus = ({text, badge, status}) =>  {
  if ((!text && !badge) || !status) return null

  return (
      <Space data-testid={`task-status-${status}`}>
        {badge}{text}
      </Space>
  )
}

export default SearchStatus