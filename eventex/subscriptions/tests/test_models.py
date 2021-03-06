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

    def test_paid_default_value_is_False(self):
        'Por default o paid deve ser False'
        self.assertEqual(False, self.obj.paid)



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

    def test_email_can_repeat(self):
        'Email nao e mais unico'
        s = Subscription.objects.create(name='Marcos Ribeiro', cpf='10987654321',
                                        email='marcos@ribeiro.com')
        self.assertEqual(2, s.pk)
