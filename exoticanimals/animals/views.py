from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import *


# Create your views here.
def hello(request):
    return HttpResponse('Hi, guys!')


menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'addpage'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}
        ]


def index(request):
    posts = Animals.objects.all()
    context = {'posts': posts,
               'menu': menu,
               'title': 'Главная страница'
               }
    return render(request, 'animals/index.html', context=context)


def about(request):
    context = {'menu': menu,
               'title': 'О сайте'
               }
    return render(request, 'animals/about.html', context=context)


def add_page(request):
    context = {'menu': menu,
               'title': 'Добавить статью'
               }
    return render(request, 'animals/add_page.html', context=context)


def contact(request):
    context = {'menu': menu,
               'title': 'Контакты'
               }
    return render(request, 'animals/contact.html', context=context)


def login(request):
    context = {'menu': menu,
               'title': 'Авторизация'
               }
    return render(request, 'animals/login.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h2>Упс :( '
                                '<br>Кажется, страница где-то потерялась.'
                                '<br>Или её не существует.</h2>')
