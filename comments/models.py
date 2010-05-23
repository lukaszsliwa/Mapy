# encoding: utf-8
from django.db import models
from django.contrib.auth.models import User
from maps.models import Map

class Comment(models.Model):
    WEATHER = (
        (1, 'Bezchmurnie'),
        (2, 'Pochmurnie'),
        (3, 'Deszczowo'),
        (4, 'Śnieżnie'),
    )
    PART_OF_THE_DAY = (
        (1, 'Rano'),
        (2, 'Popołudniu'),
        (3, 'Wieczorem')
    )

    user = models.ForeignKey(User)
    map = models.ForeignKey(Map)

    content = models.TextField(verbose_name='Treść')
    weather = models.IntegerField(
        null=True,
        verbose_name='Pogoda',
        choices=WEATHER)
    part_of_the_day = models.IntegerField(
        null=True,
        verbose_name='Część dnia',
        choices=PART_OF_THE_DAY)
    time = models.IntegerField(null=True, verbose_name='Czas przebycia trasy')
    created_at = models.DateTimeField(auto_now_add=True)

    def weather_name(self):
        return self.WEATHER[self.weather-1][1] if self.weather else None

    def part_of_the_day_name(self):
        return self.PART_OF_THE_DAY[self.part_of_the_day-1][1] if self.part_of_the_day else None

