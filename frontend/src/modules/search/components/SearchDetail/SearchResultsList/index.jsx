import {List} from 'antd';

const SearchResultItemStyle = {
  wordBreak: 'break-word',
  whiteSpace: 'normal'
}

const SearchResultsList = (props) => {
  return (
      <List
          {...props}
          renderItem={(result) => (
              <List.Item style={SearchResultItemStyle}>
                {result}
              </List.Item>)
      }
          locale={{emptyText: 'Нет данных'}}
      />
  )
}

export default SearchResultsList