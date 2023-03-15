from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = [
    {'title': 'Про сайт', 'url_name': 'about'},
    {'title': 'Додати публікацію', 'url_name': 'add_page'},
    {'title': 'Зворотній зв`язок', 'url_name': 'contact'},
    {'title': 'Вхід', 'url_name': 'login'},
]


def index(request):
    posts = Women.objects.all()
    context = {
        'menu': menu,
        'title': 'Головна сторінка',
        'posts': posts,
    }
    return render(request, 'women/index.html', context=context)


def about(request):
    context = {
        'title': 'Про сайт',
    }
    return render(request, 'women/about.html', context=context)


def categories(request, catid):
    if (request.GET):
        print(request.GET)
    return HttpResponse(f"<h1> Відображення категорій </h1><p>{catid}</p>")


def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=True)
    return HttpResponse(f"<h1> Відображення архіву по рокам </h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Сторінка не знайдена</h1>")
