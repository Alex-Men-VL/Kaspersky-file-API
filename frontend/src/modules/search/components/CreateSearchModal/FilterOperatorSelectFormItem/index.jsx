import {Form, Select} from 'antd';

const FilterOperatorSelectFormItem = ({name, options, disabled}) => {
  return (
      <Form.Item name={name} noStyle>
        <Select
            disabled={disabled}
            options={options}
            style={{
              width: 60,
              textAlign: 'center',
            }}
        >
        </Select>
      </Form.Item>
  )
}

export default FilterOperatorSelectFormItem