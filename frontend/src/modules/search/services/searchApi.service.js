import { HttpMethodEnum } from 'shared/constants/http'
import { baseApiService } from 'shared/services/baseApi'
import { getSearchUrl } from 'modules/search/utils';
import {SearchesApiEnum, SearchesApiTagEnum} from 'modules/search/constants';


const searchApiService = baseApiService
  .injectEndpoints({
    endpoints: (build) => ({
      getSearchList: build.query({
        providesTags: (result, error) => (error ? [] : [SearchesApiTagEnum.Searches]),
        query: () => ({
          url: SearchesApiEnum.GetSearchList,
          method: HttpMethodEnum.Get,
        }),
      }),
      getSearch: build.query({
        query: (searchId) => ({
          url: getSearchUrl(searchId),
          method: HttpMethodEnum.Get,
        }),
      }),
      createSearch: build.mutation({
        invalidatesTags: (result, error) => (error ? [] : [SearchesApiTagEnum.Searches]),
        query: (data) => ({
          url: SearchesApiEnum.GetSearchList,
          method: HttpMethodEnum.Post,
          data,
        }),
      }),
    }),
    overrideExisting: false,
  })

export const {
  useGetSearchListQuery,
  useGetSearchQuery,
  useCreateSearchMutation,
} = searchApiService
