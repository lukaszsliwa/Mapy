from django.contrib import admin
from maps.models import Map

class MapAdmin(admin.ModelAdmin):
    fields = ['name', 'city', 'tags', 'slug']
    list_display = ('name', 'city', 'tags')

admin.site.register(Map,MapAdmin)
