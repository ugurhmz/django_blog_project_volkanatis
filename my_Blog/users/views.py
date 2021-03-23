from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .form import LoginForm, RegisterForm


#________________________________________ login_view() ________________________________________

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


#________________________________________ register_view() ________________________________________
#
# def register_view(request):
#     form = UserCreationForm(request.POST or None)
#
#     if form.is_valid():
#         form.save()
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password')
#
#
#         user = authenticate(username=username, password=password)
#         login(request,user)
#
#         return redirect('index')
#
#     else:
#         form = UserCreationForm()
#
#     context = {
#         'form':form
#     }
#
#     return render(request,'users/register.html', context=context)


def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password1')
        user.set_password(password)
        user.is_staff = True #Admin paneline girmesi için..
        user.save()
        new_user = authenticate(username = user.username, password=password) #yeni kullanıcı oluşturuyoruz
        login(request,new_user) #login yapıyoruz
        return redirect('index') #ardından anasayfaya yönlendiriyoruz..

    else:
     form = RegisterForm()

     context = {
         'form':form
     }

    return render(request,'users/register.html', context=context)


#________________________________________ logout_view() ________________________________________

def logout_view(request):
    logout(request)

    messages.success(request,"Başarılı bir şekilde çıkış yaptınız")
    return redirect('index')



