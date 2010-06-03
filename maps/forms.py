# encoding: utf-8
from django import forms

"""
.. moduleauthor:: Łukasz Śliwa
.. moduleauthor:: Daniel Borzęcki
"""

class NewMapForm(forms.Form):
    """
    Klasa reprezentuje formularz umożliwiający dodawanie mapy do bazy danych.
    Atrybuty klasy:
        * :mod:`name` -- nazwa mapy
        * :mod:`tags` -- słowa kluczowe oddzielone przecinkiem
        * :mod:`city` -- miasto lub miasta
        * :mod:`latlngs` -- ciąg współrzędnych geograficznych oddzielonych średnikiem
        * :mod:`distance` -- długość trasy
        * :mod:`nelat`
        * :mod:`nelng`
        * :mod:`swlat`
        * :mod:`swlng`

    Wszystkie atrybuty są wymagane. Ukrytymi atrybutami są: :mod:`nelat`,
    :mod:`nelng`, :mod:`swlat`, :mod:`swlng`, :mod:`latlngs`. Atrybut jest ukryty jeśli nie
    występuje w formularzu, do którego użytkownik podaje niezbędne dane
    """
    name = forms.CharField(required=True, max_length=256,
        widget=forms.TextInput(attrs={'size': '38'}), label='Nazwa')
    tags = forms.CharField(required=True, max_length=512,
        widget=forms.TextInput(attrs={'size': '38'}), label='Tagi')
    city = forms.CharField(required=True, max_length=32, label='Miasto')
    latlngs = forms.CharField(required=True, widget=forms.HiddenInput)
    distance = forms.FloatField(required=True, widget=forms.HiddenInput)
    nelat = forms.FloatField(required=True, widget=forms.HiddenInput)
    nelng = forms.FloatField(required=True, widget=forms.HiddenInput)
    swlat = forms.FloatField(required=True, widget=forms.HiddenInput)
    swlng = forms.FloatField(required=True, widget=forms.HiddenInput)
