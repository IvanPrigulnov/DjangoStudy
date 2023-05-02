from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello(request):
    return HttpResponse('Hi, guys!')


menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']

def index(request):
    return render(
        request,
        'animals/index.html',
        {'menu': menu, 'title': 'Главная страница'}
    )


def about(request):
    return render(
        request,
        'animals/about.html',
        {'title': 'О сайте'}
    )
