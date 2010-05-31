# encoding: utf-8
from django.db import models
from maps.models import Map
from django.contrib.auth.models import User

class Time(models.Model):
    '''
    Klasa reprezentuje rekord z wynikiem czasowym osoby, która
    przebyła pewną trasę. Atrybuty:
        * map               - mapa
        * user              - użytkownik
        * time              - czas w sekundach
        * part_of_the_day   - część dnia
        * weather           - pogoda
        * note              - notatka
    '''
    PART_OF_THE_DAY = (
        (1, 'Rano'),
        (2, 'Popołudniu'),
        (3, 'Wieczorem')
    )
    WEATHER = (
        (1, 'Bezchmurnie'),
        (2, 'Pochmurnie'),
        (3, 'Deszczowo'),
        (4, 'Śnieżnie')
    )
    map = models.ForeignKey(Map)
    user = models.ForeignKey(User)
    rounds = models.IntegerField(verbose_name='Liczba rund')
    seconds = models.IntegerField(verbose_name='Uzyskany czas')
    distance = models.FloatField()
    part_of_the_day = models.IntegerField(choices=PART_OF_THE_DAY, verbose_name='Część dnia')
    weather = models.IntegerField(choices=WEATHER, verbose_name='Pogoda')
    note = models.TextField(verbose_name='Notatka')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self):
        '''
        Oblicza dystans przebytej trasy i zapisuje rekord do bazy
        '''
        self.distance = self.rounds * self.map.distance
        super(Time, self).save()

    @staticmethod
    def to_sec(template):
        '''
        Zamienia szablon postaci gg:mm:ss lub mm:ss na sekundy
        '''
        items, hours = map(int, template.split(':')), 0
        try:
            hours, minutes, seconds = items
        except:
            minutes, seconds = items
        return hours * 60 * 60 + minutes * 60 + seconds

    def __unicode__(self):
        hours = self.seconds / (60 * 60)
        minutes = (self.seconds - hours * 60 * 60) / 60
        seconds = (self.seconds - (hours * 60 * 60) - minutes * 60)
        if hours < 10:
            hours = '0' + str(hours)
        if minutes < 10:
            minutes = '0' + str(minutes)
        if seconds < 10:
            seconds = '0' + str(seconds)
        return '%s:%s:%s' % (hours, minutes, seconds)

    __str__ = __unicode__
