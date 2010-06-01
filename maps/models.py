# encoding: utf-8
from django.db import models
from django.template.defaultfilters import slugify
from points.models import LatLng

class Map(models.Model):
    name = models.CharField(max_length=256, verbose_name='Nazwa')
    slug = models.SlugField()
    tags = models.CharField(max_length=512, verbose_name='Tagi')
    city = models.CharField(max_length=32, verbose_name='Miasto')
    latlngs = models.TextField(verbose_name='Współrzędne')
    distance = models.FloatField(verbose_name='Dystans')
    southwest = models.ForeignKey(LatLng, related_name="%(class)s_sw")
    northeast = models.ForeignKey(LatLng, related_name="%(class)s_ne")

    def getlatlngs(self):
        '''
        Zwraca latlngs w postaci listy par liczb zmiennioprzecinkowych.
        '''
        result = []
        for p in self.latlngs.split(';'):
            if p:
                lat, lng = p.split(',')
                pair = float(lat), float(lng)
                result.append(pair)
        return result

    def jsonlatlngs(self):
        '''
        Zwraca latlngs w formacie json
        '''
	result = "["
        for p in self.latlngs.split(';'):
            if p:
                result += '['+p+'],'
        return result[:-1] + ']'

    def getcenter(self):
	'''
	Zwraca srodek mapy w oparciu o wspolrzedne krancowe
	'''
	horizontal = (self.northeast.latit + self.southwest.latit) / 2
	vertical   = (self.northeast.longi + self.southwest.longi) / 2
	return [horizontal, vertical]

    def gettags(self):
        return self.tags.split(' ')

    def save(self):
        '''
        Tworzy slug na podstawie name oraz zamienia wszystkie tagi na wersję
        slugową.
        '''
        self.slug = slugify(self.name)
        self.tags = ' '.join([ slugify(tag.strip()) for tag in self.tags.split(',') ])
        super(Map, self).save()

    def __unicode__(self):
        return self.name

    __str__ = __unicode__

