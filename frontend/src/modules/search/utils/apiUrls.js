import {SearchesApiEnum} from 'modules/search/constants';
import {generatePath} from 'react-router-dom';
import {appendSlashAtEnd} from 'shared/utils/string';

export const getSearchUrl = (searchId) =>
    appendSlashAtEnd(generatePath(SearchesApiEnum.GetSearch, { id: String(searchId) }))