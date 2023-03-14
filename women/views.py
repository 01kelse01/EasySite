from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Сторінка програми women.")


def categories(request):
    return HttpResponse("<h1> Відображення категорій </h1>")