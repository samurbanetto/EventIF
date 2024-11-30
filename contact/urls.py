from contact.views import contact, detail
from django.urls import path

app_name = 'contact'
urlpatterns = [
    path('', contact, name='new'),
    path('<int:pk>/', detail, name='detail'),
]