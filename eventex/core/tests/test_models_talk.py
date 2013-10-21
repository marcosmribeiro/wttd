# coding: utf-8
from django.test import TestCase
from eventex.core.models import Talk, Course
from eventex.core.managers import PeriodManager

class TalkModelTest(TestCase):
    def setUp(self):
        self.talk = Talk.objects.create(title=u'Introdução ao Django',
                                        description=u'Descrição da palestra',
                                        start_time='10:00')

    def test_create(self):
        self.assertEqual(1, self.talk.pk)

    def test_speakers(self):
        'Palestra tem varios Palestrante e vice-versa'
        self.talk.speakers.create(name='Marcos Ribeiro',
                                  slug='marcos-ribeiro',
                                  url='http://marcosribeiro.com')
        self.assertEqual(1, self.talk.speakers.count())

    def test_unicode(self):
        self.assertEqual(u'Introdução ao Django', unicode(self.talk))

    def test_period_manager(self):
        'Default manager da palestra deve ser uma instancia de PeriodManager'
        self.assertIsInstance(Talk.objects, PeriodManager)


class CourseModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(title=u'Tutorial Django',
                                            description=u'Descrição da palestra',
                                            start_time='10:00',
                                            slots=20)

    def test_create(self):
        self.assertEqual(1, self.course.pk)

    def test_unicode(self):
        self.assertEqual(u'Tutorial Django', unicode(self.course))

    def test_speakers(self):
        'Curso tem N palestrantes e vice-versa'
        self.course.speakers.create(name='Marcos Ribeiro',
                                    slug='marcos-ribeiro',
                                    url='http://marcosribeiro.com')
        self.assertEqual(1, self.course.speakers.count())

    def test_period_manager(self):
        'Default manager deve ser uma instancia de PeriodManager'
        self.assertIsInstance(Course.objects, PeriodManager)