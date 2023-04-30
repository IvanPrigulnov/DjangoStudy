from django.urls import path
from animals.views import hello

urlpatterns = [
    path('', hello)
]