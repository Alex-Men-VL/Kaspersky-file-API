import {Form, Modal, Input, InputNumber, DatePicker, Space} from 'antd'
import FilterOperatorSelectFormItem from './FilterOperatorSelectFormItem'
import {getOperatorOptions} from 'modules/search/utils'
import {OperatorEnum} from 'modules/search/constants'

const { TextArea } = Input

const operatorOptions = getOperatorOptions()

const CreateSearchModal = ({confirmLoading, onFinish, onCancel}) => {
  const [form] = Form.useForm()

  return (
      <Modal
          open
          confirmLoading={confirmLoading}
          onOk={form.submit}
          okText={'Создать'}
          onCancel={onCancel}
          cancelText='Отменить'
      >
        <Form
            form={form}
            initialValues={{
              size: {
                operator: OperatorEnum.Equal,
              },
              creationTime: {
                operator: OperatorEnum.Equal,
              },
            }}
            layout='vertical'
            onFinish={onFinish}
        >
          <Form.Item label='Текст' name='text'>
            <TextArea
                placeholder='Введите текст, который должен содержаться в файле'
                disabled={confirmLoading}
            />
          </Form.Item>

          <Form.Item label='Маска имени файла' name='fileMask'>
            <Input
                placeholder='Введите маску имени файла'
                disabled={confirmLoading}
            />
          </Form.Item>

          <Form.Item label='Размер' style={{marginBottom: '0px'}}>
            <Space.Compact block>
              <FilterOperatorSelectFormItem name={['size', 'operator']} options={operatorOptions} disabled={confirmLoading}/>

              <Form.Item name={['size', 'value']}>
                <InputNumber
                    placeholder='Введите размер файла'
                    disabled={confirmLoading}
                    style={{ width: '250px' }}
                />
              </Form.Item>
            </Space.Compact>
          </Form.Item>

          <Form.Item label='Дата создания' style={{marginBottom: '0px'}}>
            <Space.Compact block>
              <FilterOperatorSelectFormItem name={['creationTime', 'operator']} options={operatorOptions} disabled={confirmLoading}/>

              <Form.Item name={['creationTime', 'value']}>
                <DatePicker
                    showTime
                    placeholder='Введите дату создания'
                    disabled={confirmLoading}
                    style={{ width: '250px' }}
                />
              </Form.Item>
            </Space.Compact>
          </Form.Item>

        </Form>
      </Modal>
  )
}

export default CreateSearchModal