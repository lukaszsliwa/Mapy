# encoding: utf-8
from django import forms

class ProfileForm(forms.Form):
    username = forms.CharField(required=True, label='Użytkownik')
    password = forms.CharField(required=True, label='Hasło', widget=forms.PasswordInput)
    email = forms.EmailField(required=True, label='E-mail')

class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='Użytkownik')
    password = forms.CharField(required=True, label='Hasło', widget=forms.PasswordInput)

class EditProfileForm(forms.Form):
    first_name = forms.CharField(required=False, label='Imię')
    last_name = forms.CharField(required=False, label='Nazwisko')
    email = forms.EmailField(required=True, label='E-mail')
    password = forms.CharField(required=False, label='Hasło', widget=forms.PasswordInput)
