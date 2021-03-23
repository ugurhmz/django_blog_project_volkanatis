from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=100,label='Kullanıcı Adı')
    password = forms.CharField(max_length=100,labeL="Şifre",widget=forms.PasswordInput) #forms.PasswordInput  -> Şifre olarak görünmesi için



    #formdan gelen bilgileri kontrol etme
    def clean(self):
        username = self.cleaned_data.get('username') #sql injec, diğer saldırı inputlarını temizleyerek almaya yarar
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)#Burda Databasemizde böyle bir kullanıcı var mı, yokmu onu kontrol ediyor.

            if not user:
                raise forms.ValidationError("Kullanıcı adı ya da şifre hatalı!")

            return super(LoginForm,self).clean()





