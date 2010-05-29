from django import forms

class NewMapForm(forms.Form):
    name = forms.CharField(required=True, max_length=256,
        widget=forms.TextInput(attrs={'size': '38'}), label='Nazwa')
    tags = forms.CharField(required=True, max_length=512,
        widget=forms.TextInput(attrs={'size': '38'}), label='Tagi')
    city = forms.CharField(required=True, max_length=32, label='Miasto')
    latlngs = forms.CharField(required=True, widget=forms.HiddenInput)
    distance = forms.FloatField(required=True, widget=forms.HiddenInput)
