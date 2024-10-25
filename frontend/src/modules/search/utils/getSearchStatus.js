import {SearchStatusEnum} from 'modules/search/constants';

export const getSearchStatus = search => {return search?.finished ? SearchStatusEnum.Finished : SearchStatusEnum.InProgress}