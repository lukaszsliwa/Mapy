from django.views.generic.simple import direct_to_template
from django.shortcuts import redirect
from forms import NewPointForm
from models import Point
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

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

def show(request, map_id, slug):
    map = Map.objects.get(pk=map_id)
    comments = map.comment_set.order_by('-created_at')
    comment = Comment()
    comment.map = map
    form = CommentForm(instance=comment)
    return direct_to_template(request, 'maps/show.html', { 'map': map, 'form': form, 'comments': comments })

