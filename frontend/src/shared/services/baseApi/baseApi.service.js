import {createApi} from '@reduxjs/toolkit/query/react'
import baseQuery from './baseQuery';
import {apiPath, currentApiVersion} from './constants';
import {SearchesApiTagEnum} from 'modules/search/constants';


export const baseApiService = createApi({
  baseQuery: baseQuery({apiPath, currentApiVersion}),
  reducerPath: 'api',
  tagTypes: [
    SearchesApiTagEnum.Searches,
  ],
  endpoints: () => ({})
})
