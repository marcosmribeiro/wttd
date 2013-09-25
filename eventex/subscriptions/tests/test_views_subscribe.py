# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.models import Subscription
from eventex.subscriptions.forms import SubscriptionForm
from django.core.urlresolvers import reverse as r


class SubscribeTest(TestCase):
	def setUp(self):
		self.resp = self.client.get(r('subscriptions:subscribe'))

	def test_get(self):
		'GET /GET/ deve retornar status code 200'
		self.assertEqual(200, self.resp.status_code)

	def test_template(self):
		'Response deve ser um template renderizado'
		self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

	def test_html(self):
		'Html deve conter os seguintes inputs'
		self.assertContains(self.resp, '<form')
		self.assertContains(self.resp, '<input', 7)
		self.assertContains(self.resp, 'type="text"', 5)
		self.assertContains(self.resp, 'type="submit"')

	def test_csrf(self):
		'HTML deve conter crsf token'
		self.assertContains(self.resp, 'csrfmiddlewaretoken')

	def test_has_form(self):
		'Contexto deve ter o subscription form'
		form=self.resp.context['form']
		self.assertIsInstance(form, SubscriptionForm)

	def test_form_has_fields(self):
		'Form deve conter 4 campos'
		form = self.resp.context['form']
		self.assertItemsEqual(['name', 'email', 'cpf', 'phone'], form.fields)


class SubscribePostTest(TestCase):
    def setUp(self):
        data = dict(name='Marcos Ribeiro', cpf='12345678901',
                    email='marcos@ribeiro.com', phone='2345678')
        self.resp = self.client.post(r('subscriptions:subscribe'), data)

    def test_post(self):
        'POST valido deve ser redirecionado para /inscricao/1/'
        self.assertEqual(302, self.resp.status_code)

    def test_save(self):
        'POST valido deve ser salvo'
        self.assertTrue(Subscription.objects.exists())


class SubscribeInvalidPostTest(TestCase):
    def setUp(self):
        data = dict(name='Marcos Ribeiro', cpf=' 000000000012',
                    email='marcos@ribeiro.com', phone='2345678')
        self.resp = self.client.post(r('subscriptions:subscribe'), data)

    def test_post(self):
        'POST invalido nao deve ser redirecionado'
        self.assertEqual(200, self.resp.status_code)

    def test_form_errors(self):
        'Formulario deve conter erros'
        self.assertTrue(self.resp.context['form'].errors)

    def test_dont_save(self):
        'Nao salva os dados'
        self.assertFalse(Subscription.objects.exists())


class TemplateRegressionTest(TestCase):
    def test_template_has_non_field_errors(self):
        'Verifica se esta mostrando os non_field_errors no template'
        invalid_data = dict(name='Marcos Ribeiro', cpf='1245678901')
        response = self.client.post(r('subscriptions:subscribe'), invalid_data)

        self.assertContains(response, '<ul class="errorlist">')
