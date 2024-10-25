import {useGetSearchListQuery} from 'modules/search/services/searchApi.service';
import {useEffect} from 'react';
import {
  getErrorMessage,
  isBadRequestError,
  isErrorResponse,
} from 'shared/services/baseApi';
import {showErrorNotification} from 'shared/utils/notifications';
import {getSearchListErrMsg} from 'modules/search/constants';

export const useGetSearchList = () => {
  const state = useGetSearchListQuery()

  useEffect(() => {
    if (isErrorResponse(state.error)) {
      if (isBadRequestError(state.error)) {
        showErrorNotification(getErrorMessage(state.error))
      } else {
        showErrorNotification(getSearchListErrMsg)
      }
    }
  }, [state.error])

  return state
}