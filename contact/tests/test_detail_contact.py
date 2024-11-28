from contact.forms import ContactForm
from django.test import TestCase

class ContactFormTest(TestCase):
    def setUp(self):
        self.form = ContactForm()

    def test_has_form(self):
        expected = ['name', 'email', 'phone', 'message']
        self.assertSequenceEqual(expected, list(self.form.fields))
