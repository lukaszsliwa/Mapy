# encoding: utf-8
from django.db import models, connection

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

"""
.. moduleauthor:: Daniel Borzęcki
"""

class LatLng(models.Model):
    """
    Klasa odpowiada punktowi `GLatLng` na mapie `Google Maps`. Atrybuty:
        * :mod:`latit` -- wskazuje szerokość geograficzną
        * :mod:`longi` -- wskazuje długość geograficzną
    """
    latit = models.FloatField()
    longi = models.FloatField()

class Point(LatLng):
    """
    Każdy użytkownik może umieścić na mapie opisywalny punkt. Dziedziczy po klasie LatLng.
    Opis punktu jest ciągiem znaków nie dłuższym niż 120. Atrybuty:
        * :mod:`user` -- wskazuje obiekt użytkownika
        * :mod:`desc` -- opis punktu
    """
    user = models.ForeignKey(User)
    desc = models.CharField(max_length=120)

    def __unicode__(self):
        return "%s created point (%s,%s)" % (self.user, self.latit, self.longi)
