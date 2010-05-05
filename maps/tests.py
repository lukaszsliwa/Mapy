# encoding: utf-8

from django.test import TestCase
from models import Map
from forms import NewMapForm

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

