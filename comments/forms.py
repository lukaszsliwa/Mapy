# -*- coding: utf-8 -*-
from django import forms
from models import Comment

"""
.. moduleauthor:: Łukasz Śliwa
"""

class CommentForm(forms.ModelForm):
    """
    Klasa reprezentuje formularz do komentowania.
    """
    class Meta:
        model = Comment
        fields = ['content']


