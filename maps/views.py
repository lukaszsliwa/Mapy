from django.views.generic.simple import direct_to_template
from django.shortcuts import redirect
from forms import NewMapForm
from models import Map

def index(request, tag=None):
    if tag:
        maps = Map.objects.filter(tags__contains=tag)
    else:
        maps = Map.objects.all()
    return direct_to_template(request, 'maps/index.html', { 'maps': maps})

def new(request):
    if request.method == 'POST':
        form = NewMapForm(request.POST)
        if form.is_valid():
            map = Map()
            map.name = form.cleaned_data['name']
            map.tags = form.cleaned_data['tags']
            map.latlngs = form.cleaned_data['latlngs']
            map.city = form.cleaned_data['city']
            map.save()
            return redirect('map', slug=map.slug)
    elif request.method == 'GET':
        form = NewMapForm()
    return direct_to_template(request, 'maps/new.html', { 'form': form })

def show(request, slug):
    map = Map.objects.get(slug=slug)
    return direct_to_template(request, 'maps/show.html', { 'map': map })
