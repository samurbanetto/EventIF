from django.test import TestCase
from contact.models import Contact
from datetime import datetime


class ContactModelTest(TestCase):

    def setUp(self):
        self.obj = Contact(name="realsounding testname", email='veryreallooking@testmail.com',phone='12-12345-1234', message='this is a test')
        self.obj.save()


    def test_create(self):
        self.assertTrue(Contact.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('realsounding testname', str(self.obj))