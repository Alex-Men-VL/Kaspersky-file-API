import React from 'react'

import {Spin} from 'antd';

const SpinnerStyle = {
  display: 'flex',
  justifyContent: 'center',
  alignItems: 'center',
}

const Spinner = ({ tip, ...props }) => {
  return tip ? (
    <Spin tip={tip} style={SpinnerStyle} {...props}>
      {/**
         - div as children for preventing warning "tip only work in nest pattern"
         - setting height to prevent zero height of spinner container
         */}
      <div style={{ minHeight: 50 }}></div>
    </Spin>
  ) : (
    <Spin style={SpinnerStyle} {...props} />
  )
}

export default Spinner
