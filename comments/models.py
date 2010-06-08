# encoding: utf-8
from django.db import models
from django.contrib.auth.models import User
from maps.models import Map

"""
.. moduleauthor:: Łukasz Śliwa
"""

class Comment(models.Model):
    """
    Klasa reprezentuje komentarz. Z każdym komentarzem wiążemy atrybuty:

        * :mod:`user` -- wskazuje obiekt użytkownika
        * :mod:`map` -- wskazuje obiekt mapy, której dotyczy komentarz
        * :mod:`content` -- treść komentarza
        * :mod:`created_at` -- czas utworzenia komentarza (tworzona automatycznie)

    Wszystkie atrybuty są wymagane do utworzenia nowego komentarza.
    """
    user = models.ForeignKey(User)
    map = models.ForeignKey(Map)
    content = models.TextField(verbose_name='Treść')
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return unicode(self.content)

    __str__ = __unicode__

