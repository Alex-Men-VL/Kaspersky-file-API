import {OperatorEnum, SearchStatusEnum} from 'modules/search/constants';

export const OperatorDict = {
  [OperatorEnum.Equal]: '=',
  [OperatorEnum.GreaterThan]: '>',
  [OperatorEnum.LessThan]: '<',
  [OperatorEnum.GreaterThanEqual]: '≥',
  [OperatorEnum.LessThanEqual]: '≤',
}

export const searchStatusDict= {
  [SearchStatusEnum.InProgress]: 'В процессе',
  [SearchStatusEnum.Finished]: 'Завершен',
}