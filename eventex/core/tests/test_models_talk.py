# coding: utf-8
from django.test import TestCase
from eventex.core.models import Talk
from eventex.core.managers import PeriodManager

class TalkModelTest(TestCase):
    def setUp(self):
        self.talk = Talk.objects.create(title=u'Introdução ao Django',
                                        description=u'Descrição da palestra',
                                        start_time='10:00')

    def test_create(self):
        self.assertEqual(1, self.talk.pk)

    def test_speakers(self):
        'Palestra tem varios Palestrante e vice-versa'
        self.talk.speakers.create(name='Marcos Ribeiro',
                                  slug='marcos-ribeiro',
                                  url='http://marcosribeiro.com')
        self.assertEqual(1, self.talk.speakers.count())

    def test_unicode(self):
        self.assertEqual(u'Introdução ao Django', unicode(self.talk))

    def test_period_manager(self):
        'Default manager da palestra deve ser uma instancia de PeriodManager'
        self.assertIsInstance(Talk.objects, PeriodManager)