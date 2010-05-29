# encoding: utf-8

from django import forms
from models import Time

class TimeForm(forms.ModelForm):

    seconds = forms.CharField(required=True, label='Czas')
    weather = forms.IntegerField(required=False,
        widget=forms.Select(choices=Time.WEATHER),
        label='Pogoda')
    part_of_the_day = forms.IntegerField(required=False,
        widget=forms.Select(choices=Time.PART_OF_THE_DAY),
        label='Część dnia')
    note = forms.CharField(required=False,
        widget=forms.Textarea, label='Notatka')

    def clean_seconds(self):
        seconds = self.cleaned_data['seconds']
        return Time.to_sec(seconds)

    class Meta:
        model = Time
        fields = ['rounds', 'seconds', 'part_of_the_day', 'weather', 'note']
