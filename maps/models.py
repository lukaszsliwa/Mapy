# encoding: utf-8
from django.db import models
from django.template.defaultfilters import slugify
from points.models import LatLng

class Map(models.Model):
    """
    Każda mapa posiada nazwę, przyjazny adres utworzony na podstawie nazwy,
    słowa kluczowe, miasto, ciąg punktów z których złożona jest ścieżka,
    długość trasy w kilometrach oraz współrzędne krańcowe mapy.

    Nazwa mapy jest ciągiem znaków nieprzekraczającym 256.
    Przyjazny adres (ang. `slug`) to ciąg znaków nieprzekraczający 50.
    Słowa kluczowe
    """
    name = models.CharField(max_length=256, verbose_name='Nazwa')
    slug = models.SlugField()
    tags = models.CharField(max_length=512, verbose_name='Tagi')
    city = models.CharField(max_length=32, verbose_name='Miasto')
    latlngs = models.TextField(verbose_name='Współrzędne')
    distance = models.FloatField(verbose_name='Dystans')
    southwest = models.ForeignKey(LatLng, related_name="%(class)s_sw")
    northeast = models.ForeignKey(LatLng, related_name="%(class)s_ne")

    def getlatlngs(self):
        """
        Zwraca tablicę par (lat, lng). Atrybut :mod:`latlngs` zawiera ciąg
        znaków odpowiadających kolejnym punktom na trasie.::
            10.0,20.3;20.4,50.4;

        Powyższy ciąg zostanie zmieniony w tablicę par.
            >>> map.getlatlngs()
            [(10.0, 20.3), (20.4, 50.4)]

        """
        result = []
        for p in self.latlngs.split(';'):
            if p:
                lat, lng = p.split(',')
                pair = float(lat), float(lng)
                result.append(pair)
        return result

    def getcenter(self):
	"""
        Zwraca środek mapy w oparciu o współrzędne krańcowe trasy.
        """
	horizontal = (self.northeast.latit + self.southwest.latit) / 2
	vertical   = (self.northeast.longi + self.southwest.longi) / 2
	return [horizontal, vertical]

    def gettags(self):
        """
        Każde słowo kluczowe jest ciągiem znaków. Atrybut :mod:`tags` zawiera
        słowa kluczowe oddzielone pojedynczym odstępem.

        Metoda zwraca tablicę słów kluczowych.
            >>> map.gettags()
            ['wroclaw', 'grunwaldzka', 'rondo-regana']
        """
        return self.tags.split(' ')

    def save(self):
        """
        Zapisuje mapę do bazy danych tworząc przyjazną nazwę mapy (ang. slug)
        używaną przy tworzeniu adresów map. Zamienia słowa kluczowe na wersję
        bez polskich znaków, spacji oraz znaków interpunkcyjnych.
        """
        self.slug = slugify(self.name)
        self.tags = ' '.join([ slugify(tag.strip()) for tag in self.tags.split(',') ])
        super(Map, self).save()

    def __unicode__(self):
        return self.name

    __str__ = __unicode__

