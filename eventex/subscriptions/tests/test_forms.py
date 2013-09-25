# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):

    def test_has_fields(self):
        'Formulario deve ter 4 campos'
        form = SubscriptionForm()
        self.assertItemsEqual(['name', 'email', 'cpf', 'phone'], form.fields)

    def test_cpf_is_digit(self):
        'CPF so pode conter digito'
        form = self.make_validated_form(cpf='ABCD5678901')
        self.assertItemsEqual(['cpf'], form.errors)

    def test_cpf_has_11_digits(self):
        'CPF deve conter 11 digitos'
        form = self.make_validated_form(cpf='1234')
        self.assertItemsEqual(['cpf'], form.errors)

    def test_email_is_optional(self):
        'Email e opcional'
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)

    def test_name_must_be_captalized(self):
        'O nome deve ser captalizado'
        form = self.make_validated_form(name='MARCOS ribeiro')
        self.assertEqual('Marcos Ribeiro', form.cleaned_data['name'])

    def test_must_inform_email_or_phone(self):
        'Email e telefone sao opcionais, mas deve haver ao menos 1 dos 2'
        form = self.make_validated_form(email='', phone_0='', phone_1='')
        self.assertItemsEqual(['__all__'], form.errors)

    def make_validated_form(self, **kwargs):
        data = dict(name='Marcos Ribeiro', email='marcos@ribeiro.com',
                    cpf='12345678901', phone_0='21', phone_1='2345678')
        data.update(kwargs)
        form = SubscriptionForm(data)
        form.is_valid()

        return form
