# encoding: utf-8
from django.db import models
from django.contrib.auth.models import User
from maps.models import Map

class Comment(models.Model):
    '''
    Klasa reprezentuje komentarz. Z każdym komentarzem wiążemy atrybuty:
        * user       - użytkownik
        * map        - mapa, której dotyczy komentarz
        * content    - treść komentarza
        * created_at - czas utworzenia komentarza
    '''
    user = models.ForeignKey(User)
    map = models.ForeignKey(Map)
    content = models.TextField(verbose_name='Treść')
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        '''
        Zwraca treść komentarza
        '''
        return self.content

    __str__ = __unicode__

