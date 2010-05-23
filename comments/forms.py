# -*- coding: utf-8 -*-
from django import forms
from models import Comment

class CommentForm(forms.ModelForm):
    time = forms.IntegerField(required=False, label='Czas przebycia trasy')
    weather = forms.IntegerField(
        widget=forms.RadioSelect(choices=Comment.WEATHER),
        label='Pogoda', required=False)
    part_of_the_day = forms.IntegerField(
        widget=forms.RadioSelect(choices=Comment.PART_OF_THE_DAY),
        label='Część dnia', required=False)
    class Meta:
        model = Comment
        fields = ['content', 'time', 'weather', 'part_of_the_day']


