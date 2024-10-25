import { useEffect } from 'react'
import { getErrorMessage, isBadRequestError, isErrorResponse, isNotFoundError } from 'shared/services/baseApi'
import { showErrorNotification } from 'shared/utils/notifications'
import {useCreateSearchMutation} from 'modules/search/services/searchApi.service';
import {createSearchErrMsg} from 'modules/search/constants';

export const useCreateSearch = () => {
  const [mutation, state] = useCreateSearchMutation()

  useEffect(() => {
    if (isErrorResponse(state.error)) {
      if (isBadRequestError(state.error) || isNotFoundError(state.error)) {
        showErrorNotification(getErrorMessage(state.error))
      } else {
        showErrorNotification(createSearchErrMsg)
      }
    }
  }, [state.error])

  return [mutation, state]
}
