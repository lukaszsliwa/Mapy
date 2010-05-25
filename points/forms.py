from django import forms

class NewPointForm(forms.Form):
    desc = forms.CharField(required=True, max_length=120, label='Opis')
    latit = forms.CharField(required=True, widget=forms.HiddenInput)
    longi = forms.CharField(required=True, widget=forms.HiddenInput)
