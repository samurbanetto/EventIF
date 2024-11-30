from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from contact.forms import ContactForm
from django.core import mail
from django.template.loader import render_to_string
from django.conf import settings
from contact.models import Contact

# Create your views here.

def contact(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)
    

def new(request):
    return render(request, 'contact/contact_form.html', {'form': ContactForm()})


def create(request):
    form = ContactForm(request.POST)
    if not form.is_valid():
        return render(request, 'contact/contact_form.html', {'form': form})
    contact = Contact.objects.create(**form.cleaned_data)
    _send_mail('contact/contact_email.txt',{'contact': contact},'Novo contato aguardando resposta.',settings.DEFAULT_FROM_EMAIL,contact.email)
    return HttpResponseRedirect('/contact/{}/'.format(contact.pk))


def detail(request, pk):
    try:
        contact = Contact.objects.get(pk=pk)
    except Contact.DoesNotExist:
        raise Http404
    return render(request, '/contact_detail.html', {'contact': contact})


def _send_mail(template_name, context, subject, from_, to):
    body = render_to_string(template_name, context)
    email = mail.send_mail(subject, body, from_, [from_, to])