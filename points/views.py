# encoding: utf-8
from django.views.generic.simple import direct_to_template
from django.shortcuts import redirect
from forms import NewPointForm
from models import Point
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

"""
.. moduleauthor:: Daniel Borzęcki
"""

@login_required
def new(request):
    """
    Funkcja zwraca stronę z formularzem do dodania nowego punktu lub dodaje punkt
    w zależności od typus żądania: GET (utwórz formularz) lub POST (zapisz formularz).

    .. include:: ../source/login_required.rst
    """
    if request.method == 'POST':
    	form = NewPointForm(request.POST)
        if form.is_valid():
            point = Point()
            point.user = request.user
            point.desc = form.cleaned_data['desc']
            point.latit = float(form.cleaned_data['latit'])
            point.longi = float(form.cleaned_data['longi'])
            point.save()
    return HttpResponseRedirect('/')

def points_in_bounds(request, SWLat, SWLng, NELat, NELng):
    """
    Metoda zwraca stronę zawierającą punkty zapisane w formacie JSON zawarte 
    w podanym obszarze wyznaczanym przez dwa punkty - `SouthWest`, `NorthEast`.

    :param SWLat: szerokość geograficzna punktu SouthWest
    :param SWLng: długość geograficzna punktu SouthWest
    :param NELat: szerokość geograficzna punktu NorthEast
    :param NELng: długość geograficzna punktu NorthEast
    :returns: listę punktów i ich opisów w formacie JSON
    
    """
    points = Point.objects.filter(latit__gte=SWLat).filter(longi__gte=SWLng)
    points = points.filter(latit__lte=NELat).filter(longi__lte=NELng)
    result = "{\"points\" : [ "
    for point in points:
	result += "{ \"lat\":%s,\"lng\":%s,\"desc\":\"%s\" }," % (point.latit, point.longi, point.desc)
    result = result[:-1] + "]}"
    return HttpResponse( result )

