# coding: utf-8
from django.test import TestCase
from eventex.core.models import Speaker


class SpeakerModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker(name='Marcos Ribeiro',
                               slug='marcos-ribeiro',
                               url='http://marcosribeiro.com',
                               description='Developer')
        self.speaker.save()

    def test_create(self):
        'Instancia de Speaker deve ser salva'
        self.assertEqual(1, self.speaker.pk)

    def test_unicode(self):
        'unicode de Speaker deve ser o nome'
        self.assertEqual(u'Marcos Ribeiro', unicode(self.speaker))