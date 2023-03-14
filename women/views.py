from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Сторінка програми women.")


def categories(request, catid):
    if (request.GET):
        print(request.GET)
    return HttpResponse(f"<h1> Відображення категорій </h1><p>{catid}</p>")


def archive(request, year):
    return HttpResponse(f"<h1> Відображення архіву по рокам </h1><p>{year}</p>")
