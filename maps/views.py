# encoding: utf-8
from django.views.generic.simple import direct_to_template
from django.shortcuts import redirect
from forms import NewMapForm
from points.forms import NewPointForm
from models import Map
from points.models import LatLng
from comments.forms import CommentForm
from comments.models import Comment
from favorites.models import Favorite
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

"""
.. moduleauthor:: Łukasz Śliwa
.. moduleauthor:: Daniel Borzęcki
"""

ADDED = 'Trasa została dodana.'

def index(request):
    """
    Zwraca listę wszystkich map dostępnych w serwisie. Jeśli ustawiony jest
    parametr :mod:`m` to wtedy zwraca list map z miasta o wartości :mod:`m`.
    Jeśli ustawiony jest parametr :mod:`tag` to w liście pojawiają się mapy,
    które opisano słowem kluczowym :mod:`tag`.::
    
        /mapy/?m=Wrocław
        /mapy/?tag=sienkiewicza
        /mapy/?m=Wrocław&tag=sienkiewicza
        
    """
    maps = Map.objects.all()
    if request.GET:
	if "tag" in request.GET:
	   maps = maps.filter(tags__contains=request.GET['tag'])
	if "m" in request.GET:
	   maps = maps.filter(city=request.GET['m'])
    return direct_to_template(request, 'maps/index.html', { 'maps': maps})

def new(request):
    """
    Funkcja zwraca stronę z formularzem do dodania nowej mapy lub zapisuje mapę
    w zależności od typus żądania: GET (utwórz formularz) lub POST (zapisz formularz).
    """
    formpoint = NewPointForm()
    if request.method == 'POST':
        form = NewMapForm(request.POST)
        if form.is_valid():
            map = Map()
            southwest  = LatLng()
            northeast  = LatLng()
            map.name = form.cleaned_data['name']
            map.tags = form.cleaned_data['tags']
            map.latlngs = form.cleaned_data['latlngs']
            map.city = form.cleaned_data['city']
            map.distance = form.cleaned_data['distance']
	    southwest.latit = form.cleaned_data['swlat']
	    southwest.longi = form.cleaned_data['swlng']
	    northeast.latit = form.cleaned_data['nelat']
	    northeast.longi = form.cleaned_data['nelng']
	    southwest.save()
	    northeast.save()
	    map.southwest = southwest
	    map.northeast = northeast
	    map.save()
            messages.success(request, ADDED)
            return redirect('map', slug=map.slug, map_id=map.id)
    elif request.method == 'GET':
        form = NewMapForm()
    return direct_to_template(request, 'maps/new.html', { 'form': form, 'formp': formpoint })

def show(request, map_id, slug):
    """
    Metoda zwraca stronę mapy o wskazanym :mod:`map_id`.

    :param map_id: identyfikator mapy w bazie danych
    :param slug: przyjazny adres mapy, ułatwia wyszukiwanie mapy w pasku przeglądarki
    :returns: obiekt mapy, formularz komentarza, komentarze
    
    """
    map = Map.objects.get(pk=map_id)
    comments = map.comment_set.order_by('-created_at')
    times = map.time_set.order_by('-created_at')[:10]
    comment = Comment()
    comment.map = map
    form = CommentForm(instance=comment)
    return direct_to_template(request, 'maps/show.html', { 'map': map, 'form': form, 'times': times,\
						 'comments': comments, 'center' : map.getcenter() })

def maps_in_bounds(request, SWLat, SWLng, NELat, NELng):
    from django.db.models import Q
    swInBound = Q(southwest__latit__gte=SWLat) & Q(southwest__latit__lte=NELat) & \
		Q(southwest__longi__gte=SWLng) & Q(southwest__longi__lte=NELng)
    neInBound = Q(northeast__latit__gte=SWLat) & Q(northeast__latit__lte=NELat) & \
		Q(northeast__longi__gte=SWLng) & Q(northeast__longi__lte=NELng)
    seInBound = Q(northeast__latit__gte=SWLat) & Q(northeast__latit__lte=NELat) & \
		Q(southwest__longi__gte=SWLng) & Q(southwest__longi__lte=NELng)
    nwInBound = Q(southwest__latit__gte=SWLat) & Q(southwest__latit__lte=NELat) & \
		Q(northeast__longi__gte=SWLng) & Q(northeast__longi__lte=NELng)

    mapy = Map.objects.filter(swInBound | neInBound | seInBound | nwInBound )
    result = "{\"maps\" : [ "
    for mapa in mapy:
	result += "{ \"latlngs\":%s,\"id\":%s,\"slug\":\"%s\" }," % (mapa.jsonlatlngs(),mapa.id,mapa.slug)
    result = result[:-1] + "]}"
    return HttpResponse( result )


@login_required
def like(request, map_id, slug):
    """
    Dodaje mapę do ulubionych zalogowanego użytkownika.

    :param map_id: identyfikator mapy w bazie danych
    :param slug: przyjazny adres mapy
    :returns: pusty obiekt HttpResponse

    Funkcja jest wywoływana asynchronicznie przez metodę javascript.

    .. include:: ../source/login_required.rst

    """
    if request.method == 'POST':
        map = Map.objects.get(pk=map_id)
        try:
            Favorite.objects.favorite_for_user(map, request.user)
        except ObjectDoesNotExist:
            Favorite.objects.create_favorite(map, request.user)
    return HttpResponse()

@login_required
def unlike(request, map_id, slug):
    """
    Usuwa mapę z ulubionych zalogowanego użytkownika.

    :param map_id: identyfikator mapy w bazie danych
    :param slug: przyjazny adres mapy
    :returns: pusty obiekt HttpResponse

    Funkcja jest wywoływana asynchronicznie przez metodę javascript.

    .. include:: ../source/login_required.rst

    """
    if request.method == 'POST':
        map = Map.objects.get(pk=map_id)
        favorite = Favorite.objects.favorite_for_user(map, request.user)
        if favorite:
            favorite.delete()
    return HttpResponse()
