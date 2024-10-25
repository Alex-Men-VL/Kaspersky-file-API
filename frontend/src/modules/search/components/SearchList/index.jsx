import {List} from 'antd'
import {getSearchIdTitle} from 'modules/search/utils'
import SearchParams from 'modules/search/components/SearchParams';


const SearchList = ({onClickRow, ...props}) => {
  return (
      <List
          {...props}
          bordered={true}
          renderItem={(item) => (
              <List.Item key={item.searchId} onClick={() => onClickRow(item)}>
                <List.Item.Meta
                    title={getSearchIdTitle(item.searchId)}
                    description={<SearchParams params={item.searchFilter} />}
                />
              </List.Item>
          )}
          locale={{emptyText: 'Список запросов пуст'}}
      />
  )
}

export default SearchList