from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .forms import *
from .models import *


def index(request):
    posts = Animals.objects.all()

    context = {'posts': posts,
               'title': 'Главная страница',
               'cat_selected': 0
               }
    return render(request, 'animals/index.html', context=context)


def about(request):
    context = {'title': 'О сайте'}

    return render(request, 'animals/about.html', context=context)


def add_page(request):
    form = AddPostForm()
    context = {'form': form, 'title': 'Добавить статью'}

    return render(request, 'animals/add_page.html', context=context)


def contact(request):
    context = {'title': 'Контакты'}

    return render(request, 'animals/contact.html', context=context)


def login(request):
    context = {'title': 'Авторизация'}

    return render(request, 'animals/login.html', context=context)


def show_post(request, post_slug):
    post = get_object_or_404(Animals, slug=post_slug)

    context = {
        'post': post,
        'title': post.title,
        'cat_selected': post.cat_id
    }

    return render(request, 'animals/post.html', context=context)


def show_category(request, cat_slug):
    cat = Category.objects.filter(slug=cat_slug)
    posts = Animals.objects.filter(cat_id=cat[0].id)

    if len(posts) == 0:
        return HttpResponse('Скоро тут будет что-то интересное!')
        # raise Http404()

    context = {'posts': posts,
               'title': f'Отображение по категориям - {posts[0].cat}',
               'cat_selected': cat_slug}

    return render(request, 'animals/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h2>Упс :( '
                                '<br>Кажется, страница где-то потерялась.'
                                '<br>Или её не существует.</h2>')
