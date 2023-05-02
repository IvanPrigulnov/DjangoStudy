from django.urls import path
from animals.views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about')
]
