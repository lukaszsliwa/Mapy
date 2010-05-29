from django.views.generic.simple import direct_to_template
from django.shortcuts import redirect
from forms import NewPointForm
from models import Point
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

@login_required
def new(request):
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

def show(request, SWLat, SWLng, NELat, NELng):
    points = Point.objects.filter(latit__gte=SWLat).filter(longi__gte=SWLng)
    points = points.filter(latit__lte=NELat).filter(longi__lte=NELng)
    result = "{\"points\" : [ "
    for point in points:
	result += "{ \"lat\":%s,\"lng\":%s,\"desc\":\"%s\" }," % (point.latit, point.longi, point.desc)
    result = result[:-1] + "]}"
    return HttpResponse( result )

