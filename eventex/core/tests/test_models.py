# coding: utf-8
from django.test import TestCase
from eventex.core.models import Speaker, Contact
from django.core.exceptions import ValidationError


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


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(name='Marcos Ribeiro',
                                              slug='marcos-ribeiro',
                                              url='http://marcosribeiro.com',
                                              description='Developer')

    def test_email(self):
        contact = Contact.objects.create(speaker = self.speaker,
                                         kind = 'E',
                                         value = 'marcos@ribeiro.com')
        self.assertEqual(1, contact.pk)

    def test_phone(self):
        contact = Contact.objects.create(speaker = self.speaker,
                                         kind = 'P',
                                         value = '21-2345678')
        self.assertEqual(1, contact.pk)

    def test_fax(self):
        contact = Contact.objects.create(speaker = self.speaker,
                                         kind = 'F',
                                         value = '21-2345678')
        self.assertEqual(1, contact.pk)

    def test_kind(self):
        'Tipo de contato deve ser E, P ou F'
        contact = Contact.objects.create(speaker = self.speaker,
                                         kind = 'A',
                                         value = 'B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_unicode(self):
        'A representação de um contato deve ser o valor'
        contact = Contact.objects.create(speaker = self.speaker,
                                         kind = 'E',
                                         value = 'marcos@ribeiro.com')
        self.assertEqual(u'marcos@ribeiro.com', unicode(contact))
