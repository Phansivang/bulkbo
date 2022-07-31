import requests
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import sender_number,sender_name,CustomUser
from .forms import register, LoginForm
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import User
@login_required(login_url='login')
def homepage(request):
    get_balance = requests.get(
        'https://gateway.sms77.io/api/balance?p=')
    return render(request, 'home.html', {'balance': get_balance.text})


def registerview(request):
    if request.method == 'POST':
        form = register(data=request.POST)
        print(form.is_valid())
        if form.is_valid():

            print(1)
            form.save()
            messages.success(request, 'Register successfully!')
            return redirect('/login')
    else:
        form = register()
        print(2)
    print(3)
    return render(request, 'register.html', {'form': form})


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'login.html'


def senderprofileview(request):
    sendername = sender_name.objects.filter(author=request.user.id)
    print(1)
    if request.method == 'POST':
        print(2)
        check_form_sender_name = request.POST['senderid']
        if check_form_sender_name == 'phansivang':
            print(check_form_sender_name)
            save = sendername.create(author=get_user_model, sendername=check_form_sender_name)
            save.save()
    return render(request,'config.html')