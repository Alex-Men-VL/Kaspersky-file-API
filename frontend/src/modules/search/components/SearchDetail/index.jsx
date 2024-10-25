import {Divider, Drawer, Space, Typography} from 'antd';
import {useGetSearch} from 'modules/search/hooks/useGetSearch';
import {getSearchIdTitle} from 'modules/search/utils';
import LoadingArea from 'components/LoadingArea';
import SearchStatus from 'modules/search/components/SearchDetail/SearchStatus';
import {searchStatusDict} from 'modules/search/constants';
import {badgeBySearchStatus} from 'modules/search/components/SearchDetail/SearchStatus/constants';
import {useMemo} from 'react';
import {getSearchStatus} from 'modules/search/utils';
import SearchResultsList from 'modules/search/components/SearchDetail/SearchResultsList';
import SearchParams from 'modules/search/components/SearchParams';
import SearchDetailTitle from 'modules/search/components/SearchDetail/SearchDetailTitle';

const { Text, Title } = Typography

const SearchDetail = ({search, onClose}) => {

  const { currentData: searchData, isFetching: searchDataIsFetching, refetch: refetchSearchData } = useGetSearch(search.searchId)

  const status = useMemo(
      () => getSearchStatus(searchData),
      [searchData],
  )

  const title = searchData && (
      <SearchDetailTitle
          searchId={search.searchId}
          onReload={refetchSearchData}
      />
  )

  return (
      <Drawer
          closable
          destroyOnClose
          open={!!search}
          size='large'
          title={title}
          placement='right'
          onClose={onClose}
      >
        <LoadingArea isLoading={searchDataIsFetching} tip={'Загрузка карточки запроса'}>
          <Space direction='vertical' size='small'>
            {searchData && (
                <SearchStatus
                    status={status}
                    text={searchStatusDict[status]}
                    badge={badgeBySearchStatus[status]}
                />
            )}

            <Divider />

            {search.searchFilter && (
                <>
                  <Text type='secondary'>Параметры запроса:</Text>
                  <SearchParams params={search.searchFilter}/>
                </>
            )}

            <Divider />

            {searchData?.finished && (
                <>
                  <Text type='secondary'>Результат поиска:</Text>
                  <SearchResultsList dataSource={searchData.results} />
                </>
            )

            }
          </Space>
        </LoadingArea>

      </Drawer>
  )
}

export default SearchDetail