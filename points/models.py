from django.db import models, connection

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

class Point(models.Model):
    user = models.ForeignKey(User)
    desc = models.CharField(max_length=120, verbose_name='Tagi')
    latit = models.FloatField()
    longi = models.FloatField()

    def __unicode__(self):
        return "%s created point (%s,%s)" % (self.user, self.latit, self.longi)
