from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def hello(request):
    return HttpResponse('Hi, guys!')


menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}
        ]


def index(request):
    posts = Animals.objects.all()
    return render(
        request,
        'animals/index.html',
        {'posts': posts,
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
