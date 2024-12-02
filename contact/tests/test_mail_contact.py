from django.core import mail
from django.test import TestCase

class ContactPostValid(TestCase):

    def setUp(self):
        data = dict(name="realsounding testname", email='contato@eventif.com.br',
                    phone='12-12345-1234', message='this is a test')
        self.client.post('/contact/', data)
        self.email = mail.outbox[0]
    
    
    def test_contact_email_subject(self):
        expect = 'Novo contato aguardando resposta.'
        self.assertEqual(expect, self.email.subject)
    
    def test_contact_email_from(self):
        expect = 'contato@eventif.com.br'
        self.assertEqual(expect, self.email.from_email)
    
    def test_contact_email_to(self):
        expect = ['contato@eventif.com.br', 'contato@eventif.com.br']
        self.assertEqual(expect, self.email.to)
    def test_contact_Email_body(self):
        contents = ('realsounding testname','contato@eventif.com.br','12-12345-1234','this is a test')
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)