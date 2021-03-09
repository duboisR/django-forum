from django.urls import path, include

import main.views


main_urlpatterns = [
    path('login/', main.views.LoginTemplateView.as_view(), name='login'),
    path('register/', main.views.RegisterTemplateView.as_view(), name='register'),
    path('reset_pwd_form/', main.views.ResetPwdFormTemplateView.as_view(), name='reset_pwd_form'),
    path('reset_pwd_done/', main.views.ResetPwdDoneTemplateView.as_view(), name='reset_pwd_done'),
    path('reset_pwd_confirm/', main.views.ResetPwdConfirmTemplateView.as_view(), name='reset_pwd_confirm'),
    path('reset_pwd_complete/', main.views.ResetPwdCompleteTemplateView.as_view(), name='reset_pwd_complete'),
    path('profil/', main.views.ProfilTemplateView.as_view(), name='profil'),
    path('topics/', main.views.TopicListTemplateView.as_view(), name='topic_list'),
    path('topics/topic_pk/', main.views.TopicDetailTemplateView.as_view(), name='topic_detail'),
    path('topics/new/', main.views.TopicCreateTempalteView.as_view(), name='topic_create'),
    path('react/', main.views.ReactTempalteView.as_view(), name='react'),
]

urlpatterns = [
    path('', main.views.HomeTemplateView.as_view(), name='home'),
    path('main/', include(main_urlpatterns)),
]