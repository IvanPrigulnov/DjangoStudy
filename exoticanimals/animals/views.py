from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def hello(request):
    return HttpResponse('Hi, guys!')


menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']


def index(request):
    post = Animals.objects.all()
    return render(
        request,
        'animals/index.html',
        {'post': post,
         'menu': menu,
         'title': 'Главная страница'
         }
    )


def about(request):
    return render(
        request,
        'animals/about.html',
        {'menu': menu,
         'title': 'О сайте'
         }
    )
