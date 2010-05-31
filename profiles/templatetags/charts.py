# encoding: utf-8
from django import template
from django.contrib.auth.models import User
from datetime import datetime
from calendar import mdays
register = template.Library()

GOOGLE_API = 'http://chart.apis.google.com'

@register.simple_tag
def chart(username, type):
    try:
        user = User.objects.get(username=username)
        if type == '0':
            chd = {}
            month = datetime.now().month
            chxl1 = ''
            for day in range(mdays[month]):
                chd[day+1] = 0
                chxl1 += '|' + str(day+1)
            for time in user.time_set.all():
                chd[time.created_at.day] += time.distance
            max_distance, min_distance = 0, 0
            for day,distance in chd.items():
                max_distance = distance if distance > max_distance else max_distance
                min_distance = distance if distance < min_distance else min_distance
            chd = ','.join([str(distance) for day,distance in chd.items()])
            chxl2 = ''
            for y in range(min_distance, max_distance, (max_distance-min_distance)/10):
                chxl2 += '|' + str(y)
            return '%s/chart?chdl=km&chxt=x,y&cht=bvg&chxt=x,y&chxl=0:%s|1:%s&chs=750x200&chbh=10&chd=t:%s' \
                % (GOOGLE_API, chxl1, chxl2, chd)
    except User.DoesNotExist:
        return ''

