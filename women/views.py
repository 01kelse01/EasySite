from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


menu = ['Про сайт', 'Додати публікацію', 'Зворотній зв`язок', 'Вхід']


def index(request):
    context = {
        'menu': menu,
        'title': 'Головна сторінка',
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
