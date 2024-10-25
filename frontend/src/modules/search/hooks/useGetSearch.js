import {useGetSearchQuery} from 'modules/search/services/searchApi.service';
import {useEffect} from 'react';
import {isBadRequestError, isErrorResponse, isNotFoundError, isServerRangeError} from 'shared/services/baseApi';
import {showErrorNotification} from 'shared/utils/notifications';
import {getSearchNotFoundErrMsg, getSearchServerErrMsg} from 'modules/search/utils';
import {getSearchErrMsg} from 'modules/search/constants';

export const useGetSearch = (searchId, options) => {
  const state = useGetSearchQuery(searchId, options)

  useEffect(() => {
    if (isErrorResponse(state.error)) {
      if (isNotFoundError(state.error)) {
        showErrorNotification(getSearchNotFoundErrMsg(searchId))
      } else if (isBadRequestError(state.error) || isServerRangeError(state.error)) {
        showErrorNotification(getSearchServerErrMsg(searchId))
      } else {
        showErrorNotification(getSearchErrMsg)
      }
    }
  }, [searchId, state.error])

  return state
}