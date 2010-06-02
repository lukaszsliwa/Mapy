# encoding: utf-8
from django import forms

"""
.. moduleauthor:: Łukasz Śliwa
"""

class ProfileForm(forms.Form):
    """
    Reprezentuje formularz tworzenia konta. Wszystkie atrybuty są obowiązkowe
    przy uzupełnianiu formularza:
        * :mod:`username` -- nazwa użytkownika
        * :mod:`password` -- hasło
        * :mod:`email` -- adres e-mail
    """
    username = forms.CharField(required=True, label='Użytkownik')
    password = forms.CharField(required=True, label='Hasło', widget=forms.PasswordInput)
    email = forms.EmailField(required=True, label='E-mail')

class LoginForm(forms.Form):
    """
    Reprezentuje formularz do logowania. Atrybuty :mod:`username`
    oraz :mod:`password` są obowiązkowe.
    """
    username = forms.CharField(required=True, label='Użytkownik')
    password = forms.CharField(required=True, label='Hasło', widget=forms.PasswordInput)

class EditProfileForm(forms.Form):
    """
    Reprezentuje formularz edycji danych. Edycja jest uzupełniona dodatkowo
    o :mod:`first_name` oraz :mod:`last_name`, które są nieobowiązkowe.
    Jeśli pole :mod:`password` nie zostało uzupełnione to hasło nie zostanie
    zmienione.
    """
    first_name = forms.CharField(required=False, label='Imię')
    last_name = forms.CharField(required=False, label='Nazwisko')
    email = forms.EmailField(required=True, label='E-mail')
    password = forms.CharField(required=False, label='Hasło', widget=forms.PasswordInput)
