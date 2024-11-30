from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=80) #precaução, provavelmente poderia fazer um 
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.CharField(max_length=300)
    sent_on = models.DateTimeField('sent on ', auto_now_add=True)
    class Meta:
        verbose_name_plural = 'contatos'
        verbose_name = 'contato'
        ordering = ('-sent_on',)
    def __str__(self):
        return self.name
    