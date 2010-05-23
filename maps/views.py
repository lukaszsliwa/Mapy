from django.views.generic.simple import direct_to_template
from django.shortcuts import redirect
from forms import NewMapForm
from models import Map
from comments.forms import CommentForm
from comments.models import Comment
from favorites.models import Favorite
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

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
            return redirect('map', slug=map.slug, map_id=map.id)
    elif request.method == 'GET':
        form = NewMapForm()
    return direct_to_template(request, 'maps/new.html', { 'form': form })

def show(request, map_id, slug):
    map = Map.objects.get(pk=map_id)
    comments = map.comment_set.order_by('-created_at')
    comment = Comment()
    comment.map = map
    form = CommentForm(instance=comment)
    return direct_to_template(request, 'maps/show.html', { 'map': map, 'form': form, 'comments': comments })

@login_required
def like(request, map_id, slug):
    map = Map.objects.get(pk=map_id)
    if not Favorite.objects.favorite_for_user(map, request.user):
        Favorite.objects.create_favorite(map, request.user)
    return HttpResponse()
