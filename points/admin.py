from django.contrib import admin
from points.models import Point

class PointAdmin(admin.ModelAdmin):
    list_display = ('user', 'desc')

admin.site.register(Point,PointAdmin)
