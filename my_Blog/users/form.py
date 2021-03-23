from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100,label='Kullanıcı Adı')
    password = forms.CharField(max_length=100,label='Şifre',  widget=forms.PasswordInput)#forms.PasswordInput  -> Şifre olarak görünmesi için


    #formdan gelen bilgileri kontrol etme
    def clean(self):
        username = self.cleaned_data.get('username') #sql injec, diğer saldırı inputlarını temizleyerek almaya yarar
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)#Burda Databasemizde böyle bir kullanıcı var mı, yokmu onu kontrol ediyor.

            if not user:
                raise forms.ValidationError("Kullanıcı adı ya da şifre hatalı!")

            return super(LoginForm,self).clean()



class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100, label="Kullanıcı Adı")
    password1 = forms.CharField(max_length=100, label="Parola", widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, label="Parola Doğrula", widget=forms.PasswordInput)

    class Meta: #bu formun hangi modeli referans olcağını belirtiyoruz
            model = User
            fields = [
                'username',
                'password1',
                'password2'

            ]


    def clean_password2(self): #bu alanının kontrolü için
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')


        if (password1 and password2) and password1!=password2:
            #eğer her iki alanda doldurulmuşsa ve birbirine denk değilse..
            raise forms.ValidationError("Parolalar uyuşmuyor!")
        return password2