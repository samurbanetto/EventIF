from django.contrib import admin
from contact.models import Contact
from contact.models import Contact
from django import forms

# Register your models here.
from django.utils.timezone import now
from contact.models import Contact

class ContactModelAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "phone",
        "message",
        "sent_at",
        "response",
        "response_at",
        "contact_answered",
    )
    list_editable = ["response"]
    date_hierarchy = "sent_at"
    search_fields = (
        "name",
        "email",
        "phone",
        "message",
        "response",
        "response_at",
        "sent_at",
    )

    def contact_answered(self, obj):
        return obj.response != None

    contact_answered.short_description = "Contato respondido"
    contact_answered.boolean = True

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        field = super().formfield_for_dbfield(db_field, request, **kwargs)
        if db_field.name == "response":
            field.widget = forms.Textarea(
                attrs={"name": "body", "rows": "3", "cols": "15"}
            )
        return field


admin.site.register(Contact, ContactModelAdmin)
