# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.models import Subscription
from django.core.urlresolvers import reverse as r


class DetailTest(TestCase):
    def setUp(self):
        s = Subscription.objects.create(name='Marcos Ribeiro', cpf='12345678901',
                                        email='marcos@ribeiro.com', phone='2345678')
        self.resp = self.client.get(r('subscriptions:detail', args=[s.pk]))


    def test_get(self):
        'GET /inscricao/1/ deve retornar status 200'
        self.assertEqual(200, self.resp.status_code)


    def test_template(self):
        'Usar Template'
        self.assertTemplateUsed(self.resp,
                                'subscriptions/subscription_detail.html')

    def test_context(self):
        'Tem que haver uma instancia de Subscription no Contexto'
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription )

    def test_html(self):
        'Verifica se os dados de Subscription foram renderizados'
        self.assertContains(self.resp, 'Marcos Ribeiro')


class DetailNotFound(TestCase):
    def test_not_found(self):
        response = self.client.get(r('subscriptions:detail', args=[0]))
        self.assertEqual(404, response.status_code)