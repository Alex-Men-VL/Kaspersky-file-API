import {OperatorDict} from 'modules/search/constants';

export const getOperatorOptions = () => {
  return Object.entries(OperatorDict).map(([value, label]) => ({
    label,
    value,
  }))
}