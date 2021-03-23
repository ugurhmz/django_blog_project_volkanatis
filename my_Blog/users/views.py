from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .form import LoginForm



def login_view(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')


        user = authenticate(username=username, password = password) # db kontrol
        login(request,user) #kullanıcı login olsun.

        return redirect('index')


    context = {
        'form':form
    }

    return render(request,"users/login.html", context=context)
