from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

import user.models

class RegisterForm(UserCreationForm):
    class Meta:
        model = user.models.User
        fields = ('email', 'password1', 'password2', )


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('topic_list')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})