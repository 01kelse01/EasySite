from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = [
    {'title': 'Про сайт', 'url_name': 'about'},
    {'title': 'Додати публікацію', 'url_name': 'addpage'},
    {'title': 'Зворотній зв`язок', 'url_name': 'contact'},
    {'title': 'Вхід', 'url_name': 'login'},
]


def index(request):
    posts = Women.objects.all()
    context = {
        'title': 'Головна сторінка',
        'menu': menu,
        'posts': posts,
    }
    return render(request, 'women/index.html', context=context)


def about(request):
    context = {
        'title': 'Про сайт',
    }
    return render(request, 'women/about.html', context=context)


def addpage(request):
    return HttpResponse('Додати публікацію')


def contact(request):
    return HttpResponse('Зворотній зв`язок')


def login(request):
    return HttpResponse('Вхід')


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Сторінка не знайдена</h1>")
