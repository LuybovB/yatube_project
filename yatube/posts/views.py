from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Главная страница
def index(request):
    return HttpResponse('Главная страница')

# Страница сообщества
def group_posts(request, slug):
    return HttpResponse(f'Страница сообщества {slug}')

def index(request):
    template = loader.get_template('posts/index.html')
    return HttpResponse(template.render({}, request))

def group_posts(request, slug):
    return HttpResponse(f'Посты по группам {slug}')
    
def group_posts(request):
    template = 'posts/group_list.html'
    return render(request, template)