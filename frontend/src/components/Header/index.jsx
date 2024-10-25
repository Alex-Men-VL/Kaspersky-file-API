import {Col,Layout, Row, Typography} from 'antd'

const { Header: StyledHeader  } = Layout
const { Title } = Typography

const headerStyle = {
  color: '#fff',
  height: 100,
  position: 'sticky',
  top: 0,
  width: '100%',
  lineHeight: '10px',
}

const Header = () => {
  return (
      <StyledHeader style={headerStyle}>
        <Row>
          <Col>
            <Title level={3} style={{color: '#fff'}}>Тестовое задание – API поиска файлов</Title>
          </Col>
        </Row>
        <Row>
          <Col>
            Выполнил: Меньшиков Александр
          </Col>
        </Row>
      </StyledHeader>
  )
}

export default Header