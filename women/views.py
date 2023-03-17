from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
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
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=context)


def about(request):
    context = {
        'title': 'Про сайт',
    }
    return render(request, 'women/about.html', context=context)


def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                Women.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Помилка додавання публікації')
    else:
        form = AddPostForm()

    context = {
        'title': 'Додавання публікації',
        'menu': menu,
        'form': form,
    }
    return render(request, 'women/addpage.html', context=context)


def contact(request):
    return HttpResponse('Зворотній зв`язок')


def login(request):
    return HttpResponse('Вхід')


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }
    return render(request, 'women/post.html', context=context)


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    if len(posts) == 0:
        raise Http404()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Відображення по рубрикам',
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Сторінка не знайдена</h1>")
