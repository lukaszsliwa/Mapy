# encoding: utf-8
from django.views.generic.simple import direct_to_template
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from forms import TimeForm
from models import Time
from maps.models import Map
from django.contrib import messages

"""
.. moduleauthor:: Łukasz Śliwa
"""

ADDED = 'Wynik został poprawnie dodany.'
REMOVE = 'Wynik został poprawnie usunięty.'

@login_required
def new(request, map_id):
    """
    Zwraca stronę z formularzem umożliwiającym dodanie nowego wyniku.

    :returns: formularz, mapa

    .. include:: ../source/login_required.rst

    """
    form = TimeForm()
    map = Map.objects.get(pk=map_id)
    return direct_to_template(request, 'stats/new.html', { 'form': form, 'map': map })

@login_required
def add(request, map_id):
    """
    Dodaje nowy wynik na wskazanej trasie, jeśli formularz został poprawnie uzupełniony.

    :returns: formularz, mapa

    .. include:: ../source/login_required.rst

    """
    map = Map.objects.get(pk=map_id)
    form = TimeForm(request.POST)
    if form.is_valid():
        time = form.save(commit=False)
        time.map = map
        time.user = request.user
        time.save()
        messages.success(request, ADDED)
        return redirect('my-profile')
    return direct_to_template(request, 'stats/new.html', { 'form': form, 'map': map})

@login_required
def remove(request, time_id):
    """
    Usuwa wynik.

    :returns: przekierowuje na stronę użytkownika

    .. include:: ../source/login_required.rst

    """
    time = Time.objects.get(pk=time_id)
    if time.user == request.user:
        messages.success(request, REMOVE)
        time.delete()
    return redirect('my-profile')
