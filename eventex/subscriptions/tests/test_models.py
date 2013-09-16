# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.models import Subscription
from datetime import datetime
from django.db import IntegrityError


class SubscriptionTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Marcos Ribeiro',
            cpf='12345678901',
            email='marcos@ribeiro.com',
            phone='2345678'
        )

    def test_create(self):
        'Subscription deve ter name, cpf, email, phone'
        self.obj.save()
        self.assertEqual(1, self.obj.id)

    def test_has_created_at(self):
        'Subscription deve criar automaticamente o created_at'
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_unicode(self):
        self.assertEqual(u'Marcos Ribeiro', unicode(self.obj))



class SubscriptionUniqueTest(TestCase):
    def setUp(self):
        # Cria o primeiro registro para forcar a colisao
        Subscription.objects.create(name='Marcos Ribeiro', cpf='12345678901',
                                    email='marcos@ribeiro.com', phone='2345678')

    def test_cpf_unique(self):
        'CPF deve ser unico'
        s = Subscription(name='Marcos Ribeiro', cpf='12345678901',
                         email='outro@email.com', phone='2345678')
        self.assertRaises(IntegrityError, s.save)

    def test_email_unique(self):
        'Email deve ser unico'
        s = Subscription(name='Marcos Ribeiro', cpf='00000000001',
                         email='marcos@ribeiro.com', phone='2345678')
        self.assertRaises(IntegrityError, s.save)
