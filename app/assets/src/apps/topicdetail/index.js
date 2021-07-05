import React from 'react'
import ReactDOM from 'react-dom'

import TopicDetail from './TopicDetail';

var container = document.getElementById('react-topicdetail');

ReactDOM.render(
  <TopicDetail props={{...container.dataset}}/>,
  container
)
