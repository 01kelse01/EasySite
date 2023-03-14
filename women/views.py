from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'women/index.html')


def about(request):
    return render(request, 'women/about.html')


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
