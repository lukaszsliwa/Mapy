# encoding: utf-8
from maps.models import Map
from forms import CommentForm
from django.views.generic.simple import direct_to_template
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

"""
.. moduleauthor:: Łukasz Śliwa
"""

CREATED = 'Komentarz został utworzony.'

@login_required
def create(request, map_id):
    """
    Tworzy nowy komentarz do mapy.

    :param map_id: identyfikator mapy
    :returns: jeśli podano wymagane dane to tworzy komentarz i przekierowuje
              do mapy o wskazanym :mod:`map_id`, w przeciwnym wypadku generuje
              jeszcze raz i odznacza błędne pola

    .. include:: ../source/login_required.rst

    """
    map = Map.objects.get(pk=map_id)
    comments = map.comment_set.all()
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.map = map
        comment.save()
        messages.success(request, CREATED)
        return redirect('map', slug=map.slug, map_id=map.id)
    return direct_to_template(request, 'maps/show.html', { 'comments': comments, 'map': map, 'form': form })
