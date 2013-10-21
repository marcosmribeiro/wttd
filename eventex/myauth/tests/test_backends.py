# coding: utf-8
from django.contrib.auth import get_user_model
from django.test import TestCase
from eventex.myauth.backends import EmailBackend


class EmailBackendTest(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        UserModel.objects.create_user(username='marcos',
                                      email='marcos@ribeiro.com',
                                      password='123456')
        self.backend = EmailBackend()

    def test_authenticate_with_email(self):
        user = self.backend.authenticate(email='marcos@ribeiro.com',
                                         password='123456')
        self.assertIsNotNone(user)

    def test_wrong_password(self):
        user = self.backend.authenticate(email='marcos@ribeiro.com',
                                         password='errada')
        self.assertIsNone(user)

    def test_unknow_user(self):
        user = self.backend.authenticate(email='errado@ribeiro.com',
                                         password='123456')
        self.assertIsNone(user)

    def test_get_user(self):
        self.assertIsNotNone(self.backend.get_user(1))


class MultipleEmailsTest(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        UserModel.objects.create_user(username='user1',
                                      email='marcos@ribeiro.com',
                                      password='123456')
        UserModel.objects.create_user(username='user2',
                                      email='marcos@ribeiro.com',
                                      password='123456')
        self.backend = EmailBackend()

    def test_multiple_emails(self):
        user = self.backend.authenticate(email='marcos@ribeiro.com',
                                         password='123456')
        self.assertIsNone(user)


class FunctionalEmailBackendTest(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        UserModel.objects.create_user(username='marcos',
                                      email='marcos@ribeiro.com',
                                      password='123456')

    def test_login_with_email(self):
        result = self.client.login(email='marcos@ribeiro.com',
                                   password='123456')
        self.assertTrue(result)

    def test_login_with_username(self):
        result = self.client.login(username='marcos@ribeiro.com',
                                   password='123456')
        self.assertTrue(result)
