import {Layout, Spin} from 'antd'
import React from 'react'
import { Outlet } from 'react-router-dom'

import Header from 'components/Header'

const { Content } = Layout


const contentStyle = {
  display: 'flex',
  flexDirection: 'column',
  padding: '32px 20px',
};


const HomeLayout= () => {
  return (
    <Layout>
        <Header />

        <Content style={contentStyle}>
          <React.Suspense fallback={<Spin size='large' />}>
            <Outlet />
          </React.Suspense>
        </Content>
    </Layout>
  )
}

export default HomeLayout
