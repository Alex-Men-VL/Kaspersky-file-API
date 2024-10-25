import {SearchStorageKeysEnum} from 'modules/search/constants';

const getSearches = () =>
    JSON.parse(localStorage.getItem(SearchStorageKeysEnum.SearchIds)) || []

const setSearch = (search) =>
    localStorage.setItem(SearchStorageKeysEnum.SearchIds, JSON.stringify([...getSearches(), search]))


export const searchLocalStorage = {
  getSearches,
  setSearch,
}