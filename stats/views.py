# encoding: utf-8
from django.views.generic.simple import direct_to_template
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from forms import TimeForm
from maps.models import Map

@login_required
def new(request, map_id):
    form = TimeForm()
    map = Map.objects.get(pk=map_id)
    return direct_to_template(request, 'stats/new.html', { 'form': form, 'map': map })

@login_required
def add(request, map_id):
    map = Map.objects.get(pk=map_id)
    form = TimeForm(request.POST)
    if form.is_valid():
        time = form.save(commit=False)
        time.map = map
        time.user = request.user
        time.save()
        return redirect('my-profile')
    return direct_to_template(request, 'stats/new.html', { 'form': form, 'map': map})
