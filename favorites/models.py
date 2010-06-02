# encoding: utf-8
from django.db import models, connection

from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

class FavoriteManager(models.Manager):
    """
    Klasa zarządzająca dla :mod:`Favorite`
    """
    def favorites_for_user(self, user):
        """
        Zwraca ulubione obiekty dla wskazanego użytkownika

        :param user: obiekt użytkownika
        :returns: ulubione obiekty danego użytkownika

        """
        return self.get_query_set().filter(user=user)
    
    def favorites_for_model(self, model, user=None):
        """
        Zwraca ulubione obiekty określonego modelu.

        :param model: klasa modelu
        :param user: obiekt użytkownika (domyślnie None)
        :returns: ulubione obiekty danego modelu (i użytkownika)

        """
        content_type = ContentType.objects.get_for_model(model)
        qs = self.get_query_set().filter(content_type=content_type)
        if user:
            qs = qs.filter(user=user)
        return qs

    def favorites_for_object(self, obj, user=None):
        """
        Zwraca ulubione dla określonego obiektu.

        :param obj: obiekt
        :param user: obiekt użytkownika (domyślnie None)
        :returns: ulubione obiekty
        """
        content_type = ContentType.objects.get_for_model(type(obj))
        qs = self.get_query_set().filter(content_type=content_type, 
                                         object_id=obj.pk)
        if user:
            qs = qs.filter(user=user)

        return qs

    def favorite_for_user(self, obj, user):
        """
        Zwraca ulubiony obiekt dla danego użytkownika (jeśli istnieje)

        :param obj: obiekt
        :param user: użytkownik
        :return: jeśli obiekt jest skojarzony z użytkownikiem to go zwraca, w.p.p zwraca wyjątek
        :raises: ObjectDoesNotExist

        >>> user = User.objects.get(username='lukasz')
        >>> map = Map.objects.get(pk=map_id)
        >>> try:
        >>>    Favorite.objects.favorite_for_user(map, user)
        >>> except ObjectDoesNotExist:
        >>>    Favorite.objects.create_favorite(map, user)
            

        """
        content_type = ContentType.objects.get_for_model(type(obj))
        return self.get_query_set().get(content_type=content_type,
                                        object_id=obj.pk)
    
    @classmethod
    def create_favorite(cls, content_object, user):
        """
        Tworzy ulubiony obiekt dla użytkownika przez dołączenie go do tabeli.

        :param content_object: typ zawartości obiektu
        :param user: użytkownik
        :returns: utworzony obiekt
        """
        content_type = ContentType.objects.get_for_model(type(content_object))
        favorite = Favorite(
            user=user,
            content_type=content_type,
            object_id=content_object.pk,
            content_object=content_object
            )
        favorite.save()
        return favorite

class Favorite(models.Model):
    """
    Reprezentuje model łączący ulubiony obiekt użytkownika z tym użytkownikiem.
        * :mod:`user` -- wskazuje na użytkownika
        * :mod:`content_type` -- typ obiektu
        * :mod:`object_id` -- identyfikator obiektu
        * :mod:`content_object` -- wskazuje na obiekt, który lubi użytkownik
        
    """
    user = models.ForeignKey(User)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    created_on = models.DateTimeField(auto_now_add=True)
    
    objects = FavoriteManager()

    class Meta:
        verbose_name = _('favorite')
        verbose_name_plural = _('favorites')
        unique_together = (('user', 'content_type', 'object_id'),)
    
    def __unicode__(self):
        return "%s lubi %s" % (self.user, self.content_object)
