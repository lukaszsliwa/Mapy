# -*- coding: utf-8 -*-
from django import forms
from models import Comment

class CommentForm(forms.ModelForm):
    '''
    Klasa reprezentuje formularz do tworzenia komentarzy
    '''
    class Meta:
        model = Comment
        fields = ['content']


