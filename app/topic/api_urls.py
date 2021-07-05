from django.urls import path

import topic.api_views


urlpatterns = [
    path('topic/', topic.api_views.TopicListAPIView.as_view()),

    path('topic/<int:pk>/', topic.api_views.TopicRetrieveAPIView.as_view()),
    path('topic/<int:topic_pk>/message/', topic.api_views.TopicMessageCreateAPIView.as_view()),
]