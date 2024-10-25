import {SearchStatusEnum} from 'modules/search/constants';
import {Badge} from 'antd';

export const badgeBySearchStatus = {
  [SearchStatusEnum.InProgress]: <Badge status='warning' />,
  [SearchStatusEnum.Finished]: <Badge status='success' />,
}
