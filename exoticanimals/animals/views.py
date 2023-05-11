from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *


menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'addpage'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}
        ]


def index(request):
    posts = Animals.objects.all()

    context = {'posts': posts,
               'menu': menu,
               'title': 'Главная страница',
               'cat_selected': 0
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


def show_post(request, post_id):
    return HttpResponse(f'Текст статьи с id= {post_id}')


def show_category(request, cat_id):
    posts = Animals.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        return HttpResponse('Скоро тут будет что-то интересное!')
        # raise Http404()

    context = {'posts': posts,
               'menu': menu,
               'title': f'Отображение по категориям - {posts[0].cat}',
               'cat_selected': cat_id}

    return render(request, 'animals/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h2>Упс :( '
                                '<br>Кажется, страница где-то потерялась.'
                                '<br>Или её не существует.</h2>')
