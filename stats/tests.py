# encoding: utf-8
from django.test import TestCase
from models import Time
from forms import TimeForm

class TimeTest(TestCase):
    def test_to_sec(self):
        """
        Sprowadza szablon 'gg:mm:ss' do liczby sekund
        """
        for hour in range(24):
            for minute in range(60):
                for second in range(60):
                    self.assertEquals(
                        Time.to_sec('%s:%s:%s' % (hour, minute, second)),
                        hour*3600+minute*60+second)

    def test_invalid_param_in_to_sec(self):
        """
        Sprawdzenie poprawności szablonu
        """
        templates = ('10:23:v', 'aa:bb:cc', 'a:23:44', '10|23:34', '12,23,44',
        ':::', '', ':', '::')

        for template in templates:
            #Time.to_sec(template)
            self.assertRaises(Exception, Time.to_sec, (template,))

    def test___unicode__(self):
        """
        Sprawdza poprawność wypisywanego czasu
        """
        for hour in range(24):
            for minute in range(60):
                for second in range(60):
                    time = Time()
                    time.seconds = hour * 3600 + minute * 60 + second
                    self.assertEquals(
                        u'%s:%s:%s' % (hour, minute, second),
                        unicode(time), '%s:%s:%s %s' % (hour, minute, second, unicode(time)))

    def test_valid(self):
        """
        Sprawdza poprawność formularzy
        """
        form = TimeForm()
        self.assertTrue(form.is_valid(), str(form.errors))
