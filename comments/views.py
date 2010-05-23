from maps.models import Map
from forms import CommentForm
from django.views.generic.simple import direct_to_template
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def index(request):
    pass

@login_required
def create(request, map_id):
    map = Map.objects.get(pk=map_id)
    comments = map.comment_set.all()
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.map = map
        comment.save()
        return redirect('map', slug=map.slug, map_id=map.id)
    return direct_to_template(request, 'maps/show.html', { 'comments': comments, 'map': map, 'form': form })
