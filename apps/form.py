from django import forms
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

from apps.models import User

class UserRegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length = 255)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password', 'confirm_password']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')


        if password and confirm_password and password != confirm_password:
            raise ValidationError('Xatlik passwordda')
            
        return make_password(password)


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length = 255)
    password = forms.CharField(max_length = 255, widget=forms.PasswordInput)


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'type', 'email', 'about_me', 'city', 'region', 'street', 'last_name']