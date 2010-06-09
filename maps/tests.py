# encoding: utf-8

from django.test import TestCase
from models import Map
from forms import NewMapForm
from points.models import LatLng

class MapTest(TestCase):
    def test_empty_map(self):
        '''
        Tworzy pustą mapę.
        '''
        map = Map()
        self.assertFalse(map.save(), 'Mapa została zapisana')

    def test_new_empty_map_form(self):
        '''
        Tworzy pusty formularz
        '''
        form = NewMapForm(initial={})
        self.assertFalse(form.is_valid(), 'Formularz jest poprawny')

    def test_new_correct_empty_map_form(self):
        '''
        Tworzy poprawny formularz
        '''
        form = NewMapForm(initial={
            'name': 'Test',
            'tags': 'test1, test2',
            'city': 'Warszawa',
            'latlngs': '0.1,0.2;0.3,0.4;'
            })
        self.assertTrue(form.is_valid(), 'Formularz jest niepoprawny')

    def test_delete_map(self):
        '''
        Usuwa mapę po utworzeniu.
        '''
        form = NewMapForm(initial={
            'name': 'Test',
            'tags': 'test1, test2',
            'city': 'Warszawa',
            'latlngs': '0.1,0.2;0.3,0.4;'
            })
        form.is_valid()
        map = Map()
        southwest  = LatLng()
        northeast  = LatLng()
        map.name = form.cleaned_data['name']
        map.tags = form.cleaned_data['tags']
        map.latlngs = form.cleaned_data['latlngs']
        map.city = form.cleaned_data['city']
        map.distance = form.cleaned_data['distance']
        southwest.latit = form.cleaned_data['swlat']
        southwest.longi = form.cleaned_data['swlng']
        northeast.latit = form.cleaned_data['nelat']
        northeast.longi = form.cleaned_data['nelng']
        southwest.save()
        northeast.save()
        map.southwest = southwest
        map.northeast = northeast
        map.save()
        self.assertTrue(map.delete(), 'Nieprawidłowo usunięta mapa')
