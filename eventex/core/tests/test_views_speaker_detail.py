# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from eventex.core.models import Speaker


class SpeakerDetailTest(TestCase):
    def setUp(self):
        Speaker.objects.create(name='Marcos Ribeiro',
                               slug='marcos-ribeiro',
                               url='http://marcosribeiro.com',
                               description='Developer')
        url = r('core:speaker_detail', kwargs={'slug': 'marcos-ribeiro'})
        self.resp = self.client.get(url)

    def test_get(self):
        'GET deve resultar em 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Template deve estar em core/speaker_detail.html'
        self.assertTemplateUsed(self.resp, 'core/speaker_detail.html')

    def test_html(self):
        'Html deve conter os dados'
        self.assertContains(self.resp, 'Marcos Ribeiro')
        self.assertContains(self.resp, 'Developer')
        self.assertContains(self.resp, 'http://marcosribeiro.com')

    def test_context(self):
        'Speaker deve estar no contexto'
        speaker = self.resp.context['speaker']
        self.assertIsInstance(speaker, Speaker)

class SpeakerDetailNotFound(TestCase):
    def test_not_found(self):
        url = r('core:speaker_detail', kwargs={'slug': 'Samuel'} )
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)