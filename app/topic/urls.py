from django.urls import path, include

import topic.views


urlpatterns = [
    path('', topic.views.TopicListView.as_view(), name='topic_list'),
    path('topics/', topic.views.TopicListView.as_view(), name='topic_list'),
    path('topics/<int:topic_pk>/', topic.views.TopicMessageView.as_view(), name='topic_detail'),
    path('topics/new/', topic.views.TopicCreateView.as_view(), name='topic_create'),

    # React
    path('topics/react/', topic.views.TopicReactListView.as_view(), name='topic_react_list'),
    path('topics/<int:topic_pk>/react/', topic.views.TopicReactMessageView.as_view(), name='topic_react_message'),
]