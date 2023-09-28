from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from man.models import Women, Category

menu = [{"title": "О сайте", "url_name": "about"},
        {"title": "Добавить статью", "url_name": "add_page"},
        {"title": "Обратная связь", "url_name": "contact"},
        {"title": "Войти", "url_name": "login"}
]


# class WomenHome(ListView):
#     model = Women  # Атрибут, который ссылается на список статей


def index(request):
    post = Women.objects.all()
    context = {
        'post': post,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'man/index.html', context)


def show_category(request, cat_slug):
    cat_category = Category.objects.get(slug=cat_slug)
    # post = Category.objects.filter(slug=cat_category)
    post = Women.objects.filter(cat=cat_category)

    # if len(post) == 0:
    #     raise Http404()

    context = {
        'post': post,
        'menu': menu,
        # 'title': 'Главная страница',
        'title': cat_category,        
        'cat_selected': cat_category,
    }
    return render(request, 'man/index.html', context)


def about(request):
    title = Women.objects.all()
    context = {
        'title': title
    }
    return render(request, 'man/about.html', context)


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page Not Found, Sorry!!! =( </h1>')


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id
    }
    return render(request, 'man/post.html', context)
