from django.test import TestCase
from contact.forms import ContactForm

def ContactFormTest():
    def setUp(self):
        self.form = ContactForm()

def test_has_form(self):
    expected = ['name', 'email', 'phone', 'message']
    self.assertSequenceEqual(expected, list(self.form.fields))