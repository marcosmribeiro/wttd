# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscribeTest(TestCase):
	def setUp(self):
		self.resp = self.client.get('/inscricao/')

	def test_get(self):
		'GET /GET/ deve retornar status code 200'
		self.assertEqual(200, self.resp.status_code)

	def test_template(self):
		'Response deve ser um template renderizado'
		self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

	def test_html(self):
		'Html deve conter os seguintes inputs'
		self.assertContains(self.resp, '<form')
		self.assertContains(self.resp, '<input', 6)
		self.assertContains(self.resp, 'type="text"', 4)
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