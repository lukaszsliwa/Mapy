# encoding: utf-8
from django import forms

"""
.. moduleauthor:: Daniel Borzęcki
"""

class NewPointForm(forms.Form):
    """
    Klasa reprezentuje formularz umożliwiający dodawanie punktów do bazy danych.
    Atrybuty klasy:
        * :mod:`desc` -- opis punktu
        * :mod:`latit` -- szerokość geograficzna położenia punktu
        * :mod:`longi` -- długość geograficzna położenia punktu

    Wszystkie atrybuty są wymagane. Ukrytymi atrybutami są: :mod:`latit`,
    :mod:`longi`. Atrybut jest ukryty jeśli nie występuje w formularzu,
    do którego użytkownik podaje niezbędne dane.
    """

    desc = forms.CharField(required=True, max_length=120, label='Opis')
    latit = forms.CharField(required=True, widget=forms.HiddenInput)
    longi = forms.CharField(required=True, widget=forms.HiddenInput)

