# encoding: utf-8

from django import forms
from models import Time
from re import compile

"""
.. moduleauthor:: Łukasz Śliwa
.. moduleauthor:: Daniel Borzęcki
"""

seconds_re = compile(r'[0-9][0-9]:[0-9][0-9](:[0-9][0-9])?')

class TimeForm(forms.ModelForm):
    """
    Klasa reprezentuje formularz dodawania wyników.
    """
    rounds  = forms.IntegerField(required=True, label='Liczba rund')
    seconds = forms.RegexField(seconds_re,required=True, label='Czas')
    weather = forms.IntegerField(required=False,
        widget=forms.Select(choices=Time.WEATHER),
        label='Pogoda')
    part_of_the_day = forms.IntegerField(required=False,
        widget=forms.Select(choices=Time.PART_OF_THE_DAY),
        label='Część dnia')
    note = forms.CharField(required=False,
        widget=forms.Textarea, label='Notatka')

    def clean_seconds(self):
        """
        Konwertuje czas przebycia trasy z postaci gg:mm:ss na liczbę sekund.
        """
        seconds = self.cleaned_data['seconds']
        return Time.to_sec(seconds)

    def clean_rounds(self):
        """
        Konwertuje czas przebycia trasy z postaci gg:mm:ss na liczbę sekund.
        """
        rounds = self.cleaned_data['rounds']
        return max(rounds,1)


    class Meta:
        model = Time
        fields = ['rounds', 'seconds', 'part_of_the_day', 'weather', 'note']
