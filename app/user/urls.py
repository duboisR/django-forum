from django.urls import path, include

import user.views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register', user.views.register, name="register"),
]