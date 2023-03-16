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
    cats = Category.objects.all()
    context = {
        'title': 'Головна сторінка',
        'menu': menu,
        'posts': posts,
        'cats': cats,
        'cat_selected': 0,
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


def show_post(request, post_id):
    return HttpResponse(f'Відображення статті по id = {post_id}')


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    if len(posts) == 0:
        raise Http404()
    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Відображення по рубрикам',
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Сторінка не знайдена</h1>")
