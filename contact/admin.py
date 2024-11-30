from django.contrib import admin

# Register your models here.
from django.utils.timezone import now
from contact.models import Contact

class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message','sent_on', 'contacted_today')
    date_hierarchy = 'sent_on'
    search_fields = ('name', 'email', 'phone', 'message', 'sent_on')


    def contacted_today(self, obj):
        return obj.sent_on.date() == now().date()
    contacted_today.short_description = 'Contato enviado foi enviado hoje?'
    contacted_today.boolean = True
    
admin.site.register(Contact, ContactModelAdmin)