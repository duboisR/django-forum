from django.urls import path, include

import topic.views


urlpatterns = [
    path('', topic.views.TopicListView.as_view(), name='topic_list'),
    path('topics/<int:topic_pk>/', topic.views.TopicMessageView.as_view(), name='topic_detail'),
    path('topics/new/', topic.views.TopicCreateView.as_view(), name='topic_create'),
]