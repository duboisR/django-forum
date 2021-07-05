import React from 'react'
import ReactDOM from 'react-dom'

import TopicList from './TopicList';

var container = document.getElementById('react-topiclist');

ReactDOM.render(
  <TopicList props={{...container.dataset}}/>,
  container
)
