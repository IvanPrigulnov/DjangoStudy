from django.urls import path
from animals.views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('addpage/', add_page, name='addpage'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login')
]
