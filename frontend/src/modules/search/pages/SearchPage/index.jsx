import {Button, Col, Row} from 'antd';
import React, {useCallback, useState} from 'react';
import {useBoolean} from 'ahooks';
import {showErrorNotification} from 'shared/utils/notifications';
import SearchList from 'modules/search/components/SearchList';
import {useCreateSearch} from 'modules/search/hooks/useCreateSearch';
import {createSearchNotPossibleErrMsg} from 'modules/search/constants';
import {parseSearchValues} from 'modules/search/utils';
import {useGetSearchList} from 'modules/search/hooks/useGetSearchList';

const SearchDetail = React.lazy(() => import('modules/search/components/SearchDetail'))
const CreateSearchModal = React.lazy(() => import('modules/search/components/CreateSearchModal'))

const SearchPage = () => {
  const {currentData: searches, isFetching: searchesIsFetching} = useGetSearchList()

  const [selectedSearch, setSelectedSearch] = useState(undefined)

  // Открытие детальной карточки
  const [searchDetailDrawerOpened, { setTrue: openSearchDetailDrawer, setFalse: closeSearchDetailDrawer }] = useBoolean(false)

  const handleOpenSearchDetail = (record) => {
    setSelectedSearch(record)
    openSearchDetailDrawer()
  }

  const handleCloseSearchDetail = () => {
    setSelectedSearch(undefined)
    closeSearchDetailDrawer()
  }

  // Создание поиска
  const [createSearchMutation, { isLoading: createSearchIsLoading }] = useCreateSearch()

  const [createSearchModalOpened, { setTrue: openCreateSearchModal, setFalse: closeCreateSearchModal }] = useBoolean(false)

  const handleOpenCreateSearchModal = useCallback(() => {
    openCreateSearchModal()
  }, [])

  const handleCloseCreateSearchModal = useCallback(() => {
    closeCreateSearchModal()
  }, [])

  const onCreateSearch = useCallback(async (values) => {
    const parsedValues = parseSearchValues(values)
    const { text, fileMask, size, creationTime } = parsedValues

    const isAnyFieldFilled =
        text || fileMask || size?.value || creationTime?.value;

    if (!isAnyFieldFilled) {
      showErrorNotification(createSearchNotPossibleErrMsg)
      return
    }

    try {
      await createSearchMutation(parsedValues).unwrap()
      handleCloseCreateSearchModal()
    } catch (e) {
      console.error(e)
    }

  }, [createSearchMutation, handleCloseCreateSearchModal])

  return (
      <>
        <Row gutter={[0, 24]}>
          <Col span={24}>
            <Button type='primary' onClick={handleOpenCreateSearchModal}>Создать запрос</Button>
          </Col>

          <Col span={24}>
            <SearchList onClickRow={handleOpenSearchDetail} dataSource={searches} loading={searchesIsFetching} />
          </Col>
        </Row>

        {selectedSearch && searchDetailDrawerOpened && (
            <React.Suspense>
              <SearchDetail search={selectedSearch} onClose={handleCloseSearchDetail}/>
            </React.Suspense>
        )}
        
        {createSearchModalOpened && (
            <React.Suspense>
              <CreateSearchModal
                  confirmLoading={createSearchIsLoading}
                  onCancel={handleCloseCreateSearchModal}
                  onFinish={onCreateSearch}
              />
            </React.Suspense>
        )}
      </>
  )
}

export default SearchPage

