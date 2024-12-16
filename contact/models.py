from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.template.loader import render_to_string

class Contact(models.Model):
    name = models.CharField("nome", max_length=100)
    email = models.EmailField("e-mail")
    phone = models.CharField("telefone", max_length=20, null=True, blank=True)
    message = models.CharField("mensagem", max_length=200)
    sent_at = models.DateTimeField("recebido em", auto_now_add=True)
    response_at = models.DateTimeField("respondido em", null=True, blank=True)
    response = models.CharField("resposta", max_length=200, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'contatos'
        verbose_name = 'contato'
        ordering = ('-sent_at',)

    def __str__(self):
        return self.name


@receiver(post_save, sender=Contact)
def send_response_notification_email(sender, instance, **kwargs):
    if instance.response:
        data = {"name": instance.name, "phone": instance.phone if instance.phone else 'Telefone não foi informado.', "email": instance.email, "message": instance.message, "response": instance.response}
        sender.objects.filter(pk=instance.pk).update(response_at=timezone.now())
        _send_mail(
            'contact/contact_response.txt',
            {'contact': data},
            'Resposta da equipe EventIF',
            settings.DEFAULT_FROM_EMAIL,
            instance.email 
        )


def _send_mail(template_name, context, subject, from_, to):
    body = render_to_string(template_name, context)
    return send_mail(subject, body, from_, [from_, to])
