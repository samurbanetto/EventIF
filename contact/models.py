from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=80)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.CharField(max_length=300)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    class Meta:
        verbose_name_plural = 'contatos'
        verbose_name = 'contato'
        ordering = ('-created_at',)
    def __str__(self):
        return self.name
    