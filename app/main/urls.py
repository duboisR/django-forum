from django.urls import path

import main.views


urlpatterns = [
    path('', main.views.HomeTemplateView.as_view(), name='home'),
    path('login/', main.views.LoginTemplateView.as_view(), name='main_login'),
    path('register/', main.views.RegisterTemplateView.as_view(), name='main_register'),
    path('reset_pwd_form/', main.views.ResetPwdFormTemplateView.as_view(), name='main_reset_pwd_form'),
    path('reset_pwd_done/', main.views.ResetPwdDoneTemplateView.as_view(), name='main_reset_pwd_done'),
    path('reset_pwd_confirm/', main.views.ResetPwdConfirmTemplateView.as_view(), name='main_reset_pwd_confirm'),
    path('reset_pwd_complete/', main.views.ResetPwdCompleteTemplateView.as_view(), name='main_reset_pwd_complete'),
    path('profil/', main.views.ProfilTemplateView.as_view(), name='main_profil'),
    path('topics/', main.views.TopicListTemplateView.as_view(), name='main_topic_list'),
    path('topics/topic_pk/', main.views.TopicDetailTemplateView.as_view(), name='main_topic_detail'),
    path('topics/new/', main.views.TopicCreateTempalteView.as_view(), name='main_topic_create'),
    path('react/', main.views.ReactTempalteView.as_view(), name='main_react'),
]
